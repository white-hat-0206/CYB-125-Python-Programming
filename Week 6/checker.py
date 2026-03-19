#create a password checker to test strength and validation of a password before use:
import sys

print("""--------------------------------------------------
            Password Strength Checker
--------------------------------------------------
      
Welcome to the MySploit Password Strength Checker.
      
This exercise demonstrates the logical steps required
to validate passwords with varying levels of complexity.""")

allowed_symbols = "!@#$%^&*()-_+="
#banned words list, doesn't show password as invalid, only weak.
common_words = [
    "admin", "backup", "cyber", "data", "encrypt", "firewall", "guest",
    "hash", "internet", "java", "key", "login", "malware", "network",
    "oracle", "pass", "qwerty", "root", "secure", "token", "user",
    "virus", "windows", "xadmin", "yubi", "zero", "abc", "123"
]

while True:

    password = input("\nPlease enter a password to validate:\n>>> ")

    #blank password and exit program:
    if password.lower() == "exit":
        print("Exiting program...")
        sys.exit()

    
    if password.strip() == "":
        print("Empty Password")
        continue  

    reasons = []

    length = len(password)

    # Check spaces or tabs
    if " " in password or "\t" in password:
        reasons.append("Contains spaces or tabs")

    # Check for disallowed characters
    if not all(char.isalnum() or char in allowed_symbols for char in password):
        reasons.append("Contains invalid symbol(s)")

    # Check common words
    if any(word in password.lower() for word in common_words):
        reasons.append("Contains common word or phrase")

    # Character category checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in allowed_symbols for char in password)

    category_count = sum([has_upper, has_lower, has_digit, has_symbol])

    if not has_upper:
        reasons.append("Missing uppercase letter")

    if not has_lower:
        reasons.append("Missing lowercase letter")

    if not has_digit:
        reasons.append("Missing digit")

    if not has_symbol:
        reasons.append("Missing allowed symbol")

    # Length checks
    if length < 8:
        reasons.append("Too short (minimum 8 characters)")

    # Determine strength
    if (
        length >= 12 and
        category_count == 4 and
        not any(word in password.lower() for word in common_words) and
        " " not in password and
        "\t" not in password and
        all(char.isalnum() or char in allowed_symbols for char in password)
    ):
        strength = "STRONG"

    elif (
        length >= 8 and
        category_count >= 3 and
        not any(word in password.lower() for word in common_words) and
        " " not in password and
        "\t" not in password and
        all(char.isalnum() or char in allowed_symbols for char in password)
    ):
        strength = "MEDIUM"

    else:
        strength = "WEAK"

    # Output section
    print("\nResult:" + {strength})

    if strength in ["WEAK", "MEDIUM"]:
        print("Reasons:")
        for reason in reasons:
            print(reason)

    