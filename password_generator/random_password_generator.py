
import string
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
        raise ValueError("Password length must be at least 5 to accommodate required character types.")

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least 3 alphabets and 2 digits
    alphabets = [secrets.choice(string.ascii_letters) for _ in range(3)]
    digits = [secrets.choice(string.digits) for _ in range(2)]

    # Calculate remaining length
    remaining_length = length - 5
    remaining_characters = [secrets.choice(characters) for _ in range(remaining_length)]

    # Combine all characters and shuffle
    password_list = alphabets + digits + remaining_characters
    random.SystemRandom().shuffle(password_list)

    # Join to form the final password
    password = ''.join(password_list)

    return password