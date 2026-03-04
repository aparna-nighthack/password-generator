
# Gateway.md

## Overview

**Purpose:** Describes the AGX Gateway components and developer-facing flows: webhook ingestion (Event Receiver), event processing (Event Processor), MCP tools (FastMCP), and the core gateway runtime used for adapters and orchestration.

## Quick links

| Component | Path |
|-----------|------|
| Gateway runners | `agx/run_gateway_mcp.py`, `agx/run_all_services.py` |
| MCP tools | `agx/app/services/gateway_mcp/mcp.py` |
| Event Receiver | `agx/run_event_receiver.py`, `agx/app/services/event_receiver/main.py` |
| Event Processor | `agx/run_event_processor.py`, `agx/app/services/event_processor/main.py` |
| Main API / Gateway core | `agx/app/main.py`, `agx/app/core/gateway.py` |
| SQS Email consumer | `agx/run_sqs_consumer.py` |
| Env & build | `agx/.env.gateway`, `agx/Dockerfile` |

## High-level flow

1. **Ingress:** External events arrive at the Event Receiver service (webhooks for Slack, Telegram, WhatsApp, email ingestion via SQS). See `agx/app/services/event_receiver/main.py`.
2. **Validation & dedupe:** Receiver verifies signatures where applicable (Slack), checks timestamps, and deduplicates messages via Redis (functions `is_message_processed` / `mark_message_processed`).
3. **Forwarding to processor:** Valid events are forwarded via HTTP to the Event Processor at `/process-event` with `channel_type` and `channel_id` as query params.
4. **Processing:** Event Processor orchestrates the core handling:
   - Initializes or retrieves the Agent Gateway via `create_agent_gateway()` (lazy AgentGateway startup).
   - Prepares payloads, handles file downloads (Slack/Twilio media), uploads files to backend storage, and calls AGX chat APIs (via `agx_chat_service`) with developer credentials.
   - Uses adapters (e.g., Slack, WhatsApp adapters) to send responses back to users.
   - See processing flows in `agx/app/services/event_processor/main.py`.
5. **MCP Tools:** Separately, a FastMCP server exposes developer tools for gateway channels (create triggers, create apps, generate chrome extensions, etc) implemented in `agx/app/services/gateway_mcp/mcp.py`. These tools call the Gateway HTTP API (`BASE_URL`) using an agent context extracted from request headers.

## Core components & responsibilities

| Component | Port | Description | Key File |
|-----------|------|-------------|----------|
| **Event Receiver** | 8001 | Accepts webhooks, verifies and normalizes payloads, deduplicates, and forwards to Event Processor | `agx/app/services/event_receiver/main.py` |
| **Event Processor** | 8002 | The main workhorse—processes events, interacts with AGX backend, downloads/uploads attachments, and routes responses via adapters | `agx/app/services/event_processor/main.py` |
| **Agent Gateway (core)** | - | Provides adapter lifecycle, lazy Slack adapter creation, trigger scheduler, and heartbeat services. Agents/adapters are created or cached as needed | `agx/app/core/gateway.py` |
| **MCP Server** | 8006 | FastMCP server exposing developer tools; loads per-tool documentation and calls internal Gateway endpoints | `agx/app/services/gateway_mcp/mcp.py` |
| **SQS Consumer** | 8003 | Email ingestion service that consumes SQS and posts to AGX inbound endpoints | `agx/run_sqs_consumer.py` |

## Important implementation details

- **Lazy Slack adapters:** Slack adapters are created on-demand via `AgentGateway._get_or_create_slack_adapter()` and cached in Redis for metadata; tokens are always decrypted at creation time (not cached). See `agx/app/core/gateway.py`.
- **Redis-based deduplication:** Both receiver and processor use Redis to avoid duplicate processing for ~24h. Functions: `is_message_processed`, `mark_message_processed` in both services.
- **Signature & replay protection:** Slack signature verification and timestamp checks are implemented in the Event Receiver (prevents replay attacks).
- **File handling:** Files are downloaded from provider endpoints (Slack/Twilio) and uploaded to the backend via `upload_file_to_backend`. See file handling helpers in the Event Processor.
- **MCP tool docs injection:** MCP tools load Markdown docs from `app/services/gateway_mcp/tool_docs` at startup and inject into tool docstrings (dynamic docstrings).
- **Environment-driven Gateway calls:** MCP tools use `BASE_URL` / `GATEWAY_URL` to call Gateway API; the server expects a JWT (or Authorization) and `x-agent-id` headers for context.
- **Trigger scheduler & background services:** The gateway starts a trigger scheduler and Moltbook heartbeat service during `AgentGateway.start()`. See `trigger_scheduler` and `MoltbookHeartbeatService` in gateway core.

## Configuration & environment

- **Local env:** Copy example env:
- **Key env vars:** `BASE_URL` (used by MCP tools), `AGX_BASE_URL`, `AGX_API_KEY`, Redis connection, DB URL. Confirm values in `agx/.env.gateway` and other `.env` files.
- **Sensitive keys:** Slack app tokens/signing secrets are stored encrypted in DB; decryption requires the key handling configured by `SlackBotConfigService`. Slack-created app keys may also depend on `slack_app_encryption.key` when used by utilities that decrypt stored masked keys (in Event Processor).
- **Database & migrations:** Use Alembic in `agx/alembic/` with `alembic.ini` for schema migrations.

