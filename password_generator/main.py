from random_password_generator import generate_password
from password_validator import validate_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, random password.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password to be generated. Default is 12.")
    
    args = parser.parse_args()
    password_length = args.length
    
    try:
        password = generate_password(password_length)
        if validate_password(password):
            print(f"Generated Password: {password}")
        else:
            print("Generated password did not meet the validation criteria.")
    except Exception as e:
        print(f"Error generating password: {e}")

if __name__ == "__main__":
    main()