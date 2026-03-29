import secrets

def generate_password(length=12, include_special_chars=True, include_numbers=True, include_uppercase=True):
    """
    Generates a random, secure password based on specified criteria.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - include_special_chars (bool): Whether to include special characters. Default is True.
    - include_numbers (bool): Whether to include numbers. Default is True.
    - include_uppercase (bool): Whether to include uppercase letters. Default is True.
    
    Returns:
    - str: The generated password.
    """
    # Define the characters to use in the password based on parameters
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    # Securely generate a random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password