
import string
import secrets

def generate_password(length=12):
    """
    Generates a random, secure password combining letters, digits, and punctuation.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    
    Returns:
    - str: The generated password.
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Securely generate a random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password