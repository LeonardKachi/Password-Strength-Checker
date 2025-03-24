import re

def check_password_strength(password):
    # Initialize strength level
    strength = 0
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        print("Password must be at least 8 characters long.")
    # Check for lowercase and uppercase letters
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength += 1
    else:
        print("Password should include both uppercase and lowercase letters.")
    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        print("Password should include at least one number.")
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        print("Password should include at least one special character.")
    
    # Evaluate strength
    if strength == 4:
        return "Strong password!"
    elif strength == 3:
        return "Moderate password."
    else:
        return "Weak password."
    
# Take user input
password = input("Enter a password to test its strength: ")
result = check_password_strength(password)
print(result)