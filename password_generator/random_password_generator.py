import secrets

def generate_password(length=12, include_symbols=True, include_numbers=True, mixed_case=True):
    """
    Generates a random, secure password with customizable options for including symbols, numbers, and mixed case letters.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - include_symbols (bool): Whether to include special characters. Default is True.
    - include_numbers (bool): Whether to include digits. Default is True.
    - mixed_case (bool): Whether to use a mix of upper and lower case letters. Default is True.
    
    Returns:
    - str: The generated password.
    """
    characters = ''
    if mixed_case:
        characters += string.ascii_letters
    else:
        characters += string.ascii_lowercase

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password