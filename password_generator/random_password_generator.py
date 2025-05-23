import secrets
import random

def generate_password(length=12):
    """
    Generates a random, secure password combining letters, digits, and punctuation.

    Args:
    - length (int): The length of the password to generate. Default is 12.

    Returns:
    - str: The generated password.
    """
    if length < 5:
        raise ValueError("Password length must be at least 5 to include the required numeric characters.")

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    digits = string.digits

    # Ensure at least 5 numeric characters
    password_digits = [secrets.choice(digits) for _ in range(5)]
    
    # Generate the remaining characters
    remaining_length = length - 5
    password_characters = [secrets.choice(characters) for _ in range(remaining_length)]
    
    # Combine and shuffle to ensure randomness
    password_list = password_digits + password_characters
    random.shuffle(password_list)

    return ''.join(password_list)