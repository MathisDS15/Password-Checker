import math

SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
MIN_LENGTH = 8

# This function checks the password and calculates its entropy
def passwordChecker(password : str) -> dict:

    password_checker_info = {
        "valid": True,
        "errors": [],
        "strength": "Weak",
        "entropy": 0.0
    }

    lowercase_count = 0
    uppercase_count = 0
    digits_count = 0
    special_count = 0

    # Check if the password contains at least one lowercase letter, one uppercase letter,
    # one digit, and one special character
    for char in password:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char in SPECIAL_CHARS:
            special_count += 1

    # Check if the password contains at least 8 characters
    if len(password) < MIN_LENGTH:
        password_checker_info["valid"] = False
        password_checker_info["errors"].append(f"Password too short. Password must be"
                                               f" at least {MIN_LENGTH} characters long.")


    if password_checker_info["valid"]:
        char_size = 0
        if lowercase_count > 0:
            char_size += 26
        if uppercase_count > 0:
            char_size += 26
        if digits_count > 0:
            char_size += 10
        if special_count > 0:
            char_size += 33

        # Calculate the entropy of the password
        password_checker_info["entropy"] = len(password) * math.log2(char_size)

        if password_checker_info["entropy"] >= 125:
            password_checker_info["strength"] = "Very Strong"
        elif password_checker_info["entropy"] >= 60:
            password_checker_info["strength"] = "Strong"
        elif password_checker_info["entropy"] >= 33:
            password_checker_info["strength"] = "Medium"
        elif password_checker_info["entropy"] >= 28:
            password_checker_info["strength"] = "Weak"
        else:
            password_checker_info["strength"] = "Very Weak"

    return password_checker_info


# Calculate the number of possible characters in the password
def displayPasswordCheck(password : str) -> None:

    display = passwordChecker(password)
    print(f"Analyse this password: {password}")
    print(f"Validity: {"Valid" if display["valid"] else "Invalid"}")
    if display["errors"]:
        print("Errors: " + display['errors'])
    print(f"Strength: {display['strength']}")
    print(f"Entropy: {display['entropy']}")

displayPasswordCheck("Rybixe_29*")