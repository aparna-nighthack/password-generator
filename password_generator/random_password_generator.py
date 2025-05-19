import secrets

def generate_password(length=12, use_symbols=True, use_numbers=True, use_mixed_case=True):
    """
    Generates a random, secure password with options for symbols, numbers, and mixed cases.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - use_symbols (bool): Whether to include symbols in the password. Default is True.
    - use_numbers (bool): Whether to include numbers in the password. Default is True.
    - use_mixed_case (bool): Whether to include both uppercase and lowercase letters. Default is True.
    
    Returns:
    - str: The generated password.
    """
    characters = ''
    if use_mixed_case:
        characters += string.ascii_letters
    else:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password