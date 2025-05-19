
import re

def validate_password(password):
    """
    Validate the password to ensure it meets the required criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase characters
    - Contains at least one numerical digit
    - Contains at least one special character, such as @, #, $
    
    :param password: The password string to validate
    :return: True if the password is valid, False otherwise
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@#$]", password):
        return False
    return True