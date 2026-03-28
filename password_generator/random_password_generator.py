import secrets

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random, secure password with options for character types.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - use_uppercase (bool): Include uppercase letters. Default is True.
    - use_lowercase (bool): Include lowercase letters. Default is True.
    - use_digits (bool): Include digits. Default is True.
    - use_symbols (bool): Include symbols. Default is True.
    
    Returns:
    - str: The generated password.
    """
    # Define the characters to use in the password based on the flags
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    # Securely generate a random password
    while True:
        password = ''.join(secrets.choice(characters) for i in range(length))
        
        # Check for minimal complexity criteria
        if (not use_uppercase or any(c in string.ascii_uppercase for c in password)) and \
           (not use_lowercase or any(c in string.ascii_lowercase for c in password)) and \
           (not use_digits or any(c in string.digits for c in password)) and \
           (not use_symbols or any(c in string.punctuation for c in password)):
            break

    return password