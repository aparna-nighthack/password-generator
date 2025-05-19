from random_password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    parser.add_argument("--include-symbols", action="store_true", help="Include special characters in the password.")
    parser.add_argument("--include-numbers", action="store_true", help="Include digits in the password.")
    parser.add_argument("--mixed-case", action="store_true", help="Use mixed-case letters in the password.")
    
    args = parser.parse_args()
    password_length = args.length
    include_symbols = args.include_symbols
    include_numbers = args.include_numbers
    mixed_case = args.mixed_case
    
    try:
        password = generate_password(password_length, include_symbols, include_numbers, mixed_case)
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()
```

```python
import string
import secrets

def generate_password(length=12, include_symbols=True, include_numbers=True, mixed_case=True):
    characters = ''
    if mixed_case:
        characters += string.ascii_letters
    else:
        characters += string.ascii_lowercase
    
    if include_numbers:
        characters += string.digits
    
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No characters available to generate password.")
    
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password