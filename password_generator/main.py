from random_password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--uppercase", action='store_true', help="Include uppercase letters in the password.")
    parser.add_argument("--numbers", action='store_true', help="Include numerical digits in the password.")
    parser.add_argument("--special-characters", action='store_true', help="Include special characters in the password.")
    
    args = parser.parse_args()
    password_length = args.length
    include_uppercase = args.uppercase
    include_numbers = args.numbers
    include_special_characters = args.special_characters
    
    try:
        password = generate_password(password_length, include_uppercase, include_numbers, include_special_characters)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()
```

```python
import string
import secrets

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_characters=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password