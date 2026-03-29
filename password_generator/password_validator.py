*** Begin Patch
*** Create File: /home/aparna/codeshwar/testbot_v1/local_GPT2/api/v1/repository/SOURCE_DOCUMENTS-886546957/aparna-nighthack-password-generator/password_generator/validation.py

```python
import re

def validate_password(password):
    """
    Validate a password to ensure it has at least 3 alphabets, 2 numbers,
    and contains both '@' and '$' symbols.

    Parameters:
    password (str): The password to validate.

    Returns:
    bool: True if password is valid, False otherwise.
    """
    if (len(re.findall(r'[a-zA-Z]', password)) < 3 or
        len(re.findall(r'[0-9]', password)) < 2 or
        '@' not in password or
        '$' not in password):
        return False
    return True
```
*** End Patch ***