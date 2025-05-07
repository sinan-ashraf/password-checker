import math

def calculate_entropy(password):
    if len(password) == 0:
        return 0

    # Initializing checks
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # Checking each character
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Special character
            has_special = True

    # Counting character pool size
    character_options = 0
    if has_lower:
        character_options += 26
    if has_upper:
        character_options += 26
    if has_digit:
        character_options += 10
    if has_special:
        character_options += 32  # Approximate for common symbols

    if character_options == 0:
        return 0

    # Entropy calculation
    return math.log2(character_options) * len(password)

def get_recommendation(entropy):
    if entropy < 20:
        return "Too weak. Use longer passwords with a mix of uppercase, lowercase, numbers, and symbols."
    elif entropy < 30:
        return "Still weak. Try adding more characters or mixing character types."
    elif entropy < 40:
        return "Decent, but could be stronger."
    else:
        return "Strong password!"

def main():
    MIN_ENTROPY = 30

    print("\nPassword Strength Checker (Entropy-Based)")
    print("Type 'quit' to exit.")

    while True:
        pwd = input("\nEnter password: ").strip()
        if not pwd or pwd.lower() == 'quit':
            break

        entropy = calculate_entropy(pwd)
        if entropy < MIN_ENTROPY:
            print(f"Weak password ({entropy:.1f} bits entropy)")
        else:
            print(f"Strong password ({entropy:.1f} bits entropy)")
        
        print(get_recommendation(entropy))

if __name__ == "__main__":
    main()
