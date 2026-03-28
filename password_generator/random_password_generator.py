import secrets

def generate_password(length=12, min_numbers=0, min_special=0, include_uppercase=True):
    if length < min_numbers + min_special:
        raise ValueError("Password length cannot be less than the sum of minimum numbers and special characters required.")
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits
    punctuation = string.punctuation
    
    password = [
        secrets.choice(digits) for _ in range(min_numbers)
    ] + [
        secrets.choice(punctuation) for _ in range(min_special)
    ]
    
    remaining_length = length - len(password)
    characters = lowercase_letters + uppercase_letters + digits + punctuation
    password += [secrets.choice(characters) for _ in range(remaining_length)]
    
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)