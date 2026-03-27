import secrets
import argparse

def generate_password(length=12, min_digits=5):
    """
    Generates a random, secure password combining letters, digits, and punctuation.
    
    Args:
    - length (int): The length of the password to generate. Default is 12.
    - min_digits (int): Minimum number of digits required in the password. Default is 5.
    
    Returns:
    - str: The generated password.
    """
    if length < min_digits:
        raise ValueError("Password length must be at least as large as min_digits")

    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        if sum(c.isdigit() for c in password) >= min_digits:
            return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--min-digits", type=int, default=5, help="Minimum number of numeric characters in the password. Default is 5.")

    args = parser.parse_args()
    password_length = args.length
    min_digits = args.min_digits

    try:
        password = generate_password(length=password_length, min_digits=min_digits)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()