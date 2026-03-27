import random
import argparse

def generate_password(length=12):
    if length < 3:
        raise ValueError("Password length must be at least 3 to include three alphabetic characters.")

    letters = string.ascii_letters
    digits_and_punctuation = string.digits + string.punctuation
    characters = letters + digits_and_punctuation

    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if sum(c.isalpha() for c in password) >= 3:
            break

    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    
    args = parser.parse_args()
    password_length = args.length
    
    try:
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()