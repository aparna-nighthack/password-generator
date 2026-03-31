import secrets
import random

def generate_password(length=12):
    if length < 5:
        raise ValueError("Password length must be at least 5 to accommodate the required character types.")

    alphabetic_characters = string.ascii_letters
    numeric_characters = string.digits
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password_chars = random.choices(alphabetic_characters, k=3) + random.choices(numeric_characters, k=2)
    
    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_characters, k=remaining_length)
    
    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    
    return password

if __name__ == "__main__":
    print(generate_password(12))