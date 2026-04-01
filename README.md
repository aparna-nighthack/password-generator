import secrets
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument('--length', type=int, required=True, help='Length of the password')
    args = parser.parse_args()

    try:
        password = generate_password(args.length)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
