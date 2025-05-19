import secrets

def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True):
    """
    Generates a random, secure password combining letters, digits, and punctuation.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - use_symbols (bool): Whether to include symbols in the password. Default is True.
    - use_numbers (bool): Whether to include numbers in the password. Default is True.
    - use_uppercase (bool): Whether to include uppercase letters in the password. Default is True.
    
    Returns:
    - str: The generated password.
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password