import secrets
import string

def generate_password(length=12):
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a random, secure password.')
    parser.add_argument('--length', type=int, default=12, help='Specify the length of the password. Default is 12.')
    args = parser.parse_args()

    password = generate_password(args.length)
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()