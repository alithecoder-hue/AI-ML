import random
import string
import re

def generate_password():
    print("\n"+"="*50)
    print("Password Generator")
    print("="*50)

    while True:
        try:
            length = int(input("Enter Password Length(8-32):"))
            if 8 <= length <=32:
                break
            else:
                print("Length must be between 8-32")
        except ValueError:
            print("Please ENTER a valid number!")

    print("\n Include the following:")

    use_upper = input("Uppercase Letters (A-Z)? (y/n): ").lower() == 'y'
    use_lower = input("Lowercase Letters (a-z)? (y/n): ").lower() == 'y'
    use_digits = input("Numbers (0-9)? (y/n): ").lower() == 'y'
    use_symbols = input("sybmbols (!@#$%^&*)? (y/n): ").lower() == 'y'

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not char_pool:
        print("\n You must select atleast one chatracter type!")
        return None
    
    password = ''.join(random.choice(char_pool) for _ in range(length))

    print("\n"+"="*50)
    print("Generate Password: ")
    print("="*50)
    print(f"\n Password: {password}")
    print("="*50)
    
    return password

def check_strength(password):
    if not password:
        return
    print("\n"+"="*50)
    print("Password Strength Checker")
    print("="*50)
    print(f"\n Password: {password}")

    score = 0 
    feedback = []

    length = len(password)
    if length >= 12 :
        score += 3
        feedback.append("Good length (12+ Character)")
    elif length >= 8 :
        score +=2
        feedback.append("Acceptable Length (8-11 Character)")
    else:
        feedback.append("Too Short (minimum 8 characters)")

    if re.search(r'[A-Z]', password):
        score+=2
        feedback.append("Contians uppercase letters...")
    else:
        feedback.append("Add Uppercase letters (A-Z)")

    if re.search(r'[a-z]', password):
        score+=2
        feedback.append("Contians lowercase letters....")
    else:
        feedback.append("Add lowercase letters (a-z)")

    if re.search(r'/d', password):
        score+=2
        feedback.append("Contian Numbers...")
    else:
        feedback.append("Add Numbers (0-9)")

    if re.search(r'[!@#$%^&*()_+\-=[\]{}|;:,.<>?]', password):
        score+=2
        feedback.append("Contian Symbols...")
    else:
        feedback.append("Add Symbols(!@#$%^&*()_+-=[]{}|;:,.<>?)")
    
    common_patterns = ['password' , '12345678' , 'qwerty' , 'admin' , 'letmein']

    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("Contain Common Weak Patterns...")

    print("\n"+"-"*50)
    print("Strength Analysis")
    print("-"*50)

    for tip in feedback:
        print(tip)

    print("\n"+"-"*50)
    print("Strength Score")

    if score >= 9 :
        print("Very Strong - Excellent Password!")
        strength = "Very Strong"
    elif score >=7:
        print("Strong - Good Password but can be improved")
        strength = "Strong"
    elif score >= 5:
        print("Medium - Consider making it stronger")
        strength = "Medium"
    else:
        print("Weak - This password is too Weak!")
        strength = "Weak"

    print("-"*50)

    return strength

def suggest_improvement(password):

    print("\n"+"="*50)
    print("Improvement Suggestion")
    print("="*50)

    suggestions = []

    if len(password) < 10 :
        suggestions.append(f" Increase length to 12+ Characters (currently {len(password)})")

    if not re.search(r'[A-Z]', password):
        suggestions.append("Add atleast one uppercase letter")
    if not re.search(r'[a-z]', password):
        suggestions.append("Add atleast one lowercase letter")
    if not re.search(r'/d', password):
        suggestions.append("Add atleast one Number")
    if not re.search(r'[!@#$%^&*]', password):
        suggestions.append("Add atleast one Symbol")
    if suggestions:
        print("\n How to improve this password:")
        for s in suggestions:
            print(s)
        else:
            print("This Password is already Strong")
        print("Example Strong Password : MySecure@2026!pass")

def main():
    while True:
        print("\n"+"="*50)
        print("Password Tool")
        print("="*50)
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Generate+Check")
        print("4. Exit")

        choice = input("\nChoose (1-4): ")
        
        if choice== "1":
            generate_password()
        elif choice == "2":
            password = input("\n Enter password to check stength: ")
            check_strength(password)
            suggest_improvement(password)
        elif choice == "3":
            password = generate_password()
            if password:
                check_strength(password)
                suggest_improvement(password)
        elif choice == "4":
            print("\n Stay Secure! GoodBye")
        else :
            print("Invalid choice")
if __name__ == "__main__" :
    main()
          