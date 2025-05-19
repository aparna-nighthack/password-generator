from random_password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--include-symbols", action='store_true', help="Include symbols in the password.")
    
    args = parser.parse_args()
    password_length = args.length
    include_symbols = args.include_symbols
    
    try:
        password = generate_password(password_length, include_symbols)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()
```

```python
import string
import secrets

def generate_password(length=12, include_symbols=True):
    """
    Generates a random, secure password combining letters, digits, and optionally punctuation.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - include_symbols (bool): Whether to include symbols in the password. Default is True.
    
    Returns:
    - str: The generated password.
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    
    # Securely generate a random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password