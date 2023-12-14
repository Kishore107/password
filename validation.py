import re

def validate_password(password):
    # Check for minimum length
    if len(password) < 8:
        return 1, "Password is too short. It should be at least 8 characters long."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return 2, "Password should contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return 3, "Password should contain at least one lowercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return 4, "Password should contain at least one digit."

    # Check for at least one special character
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_characters.search(password):
        return 5, "Password should contain at least one special character."

    return 0, "Password is strong."

def password_strength_score(score):
    if score == 0:
        return "Strong"
    elif score == 1:
        return "Weak"
    elif score == 2 or score == 3 or score == 4 or score == 5:
        return "Moderate"
