from random_password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--uppercase", action='store_true', help="Include uppercase letters in the password.")
    parser.add_argument("--lowercase", action='store_true', help="Include lowercase letters in the password.")
    parser.add_argument("--digits", action='store_true', help="Include digits in the password.")
    parser.add_argument("--symbols", action='store_true', help="Include symbols in the password.")
    
    args = parser.parse_args()
    password_length = args.length
    include_uppercase = args.uppercase
    include_lowercase = args.lowercase
    include_digits = args.digits
    include_symbols = args.symbols

    if not (include_uppercase or include_lowercase or include_digits or include_symbols):
        print("Error: At least one character type must be selected.")
        return

    try:
        password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_symbols)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()
```

```python
import string
import secrets

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password