from random_password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password with customizable features.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--numbers", action="store_true", help="Include numbers in the password.")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters in the password.")
    parser.add_argument("--special", action="store_true", help="Include special characters in the password.")
    
    args = parser.parse_args()
    password_length = args.length
    include_numbers = args.numbers
    include_uppercase = args.uppercase
    include_special = args.special
    
    try:
        password = generate_password(password_length, include_numbers, include_uppercase, include_special)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()
```

```python
import string
import secrets

def generate_password(length=12, include_numbers=True, include_uppercase=True, include_special=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No characters available to generate password. Please enable at least one character type.")
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password