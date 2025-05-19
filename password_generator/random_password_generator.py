import secrets
import argparse

def generate_password(length=12, include_numbers=True, include_uppercase=True, include_special=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--no-numbers", action="store_false", help="Exclude numbers from the password.", dest="include_numbers")
    parser.add_argument("--no-uppercase", action="store_false", help="Exclude uppercase letters from the password.", dest="include_uppercase")
    parser.add_argument("--no-special", action="store_false", help="Exclude special characters from the password.", dest="include_special")
    
    args = parser.parse_args()
    password_length = args.length
    include_numbers = args.include_numbers
    include_uppercase = args.include_uppercase
    include_special = args.include_special
    
    try:
        password = generate_password(password_length, include_numbers, include_uppercase, include_special)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()