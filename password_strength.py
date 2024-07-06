import re

def check_password_strength(password):
    strength_score = 0
    feedback=[]

    if len(password) >= 8:
        strength_score +=1
    else:
        feedback.append("Password should be at least 8 characters long")

    #uppercase and lowercase letters
    if re.search('[A-Z]', password) and re.search('[a-z]', password):
        strength_score +=1
    else:
        feedback.append("Password should have both uppercase and lowercase letters.")
    
    #digits
    if re.search('[0-9]', password):
        strength_score +=1
    else:
        feedback.append("Password should have digits.")

    #special characters
    if re.search('[!@#$%^&*?]', password):
        strength_score +=1
    else:
        feedback.append("Password should include special characters (eg: !@#$%^&*?).")
    
    common_passwords = ["password", "12345678", "qwerty","abc123"]
    if password.lower() in common_passwords:
        feedback.append("Password is too common")
    else:
        strength_score +=1

    if strength_score == 5:
        strength= "Very Strong"
    elif strength_score == 4:
        strength= "Strong"
    elif strength_score == 3:
        strength= "Moderate"
    elif strength_score == 2:
        strength= "Weak"
    else:
        strength= "Very Weak"

    return strength, feedback

password = input("enter a password to check its strength:")
strength, feedback = check_password_strength(password)

print(f"Password strength : {strength}")
if feedback:
    print("Feedback:")
    for f in feedback:
        print(f"-{f}")

