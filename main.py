import math
from pybloom_live import ScalableBloomFilter

def calculate_entropy(password):
    if len(password) == 0:
        return 0
    
    # Initializing checks
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    # Checking each character using a simple loop
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Special character
            has_special = True
    
    # Counting how many different character options we have
    character_options = 0
    
    # Adding options for each character type found
    if has_lower: character_options += 26  # a-z
    if has_upper: character_options += 26  # A-Z
    if has_digit: character_options += 10  # 0-9
    if has_special: character_options += 32  # Common symbols
    


def load_leaked_passwords(file_path='data/leaked-passwords.txt'):
    bloom = ScalableBloomFilter(initial_capacity=10000, error_rate=0.01)
    
    # Default passwords if file doesn't exist
    default_passwords = ['123456', 'password', '12345678', 'qwerty', '123456789']
    
    try:
        with open(file_path) as f:
            passwords = (line.strip() for line in f if line.strip())
            for pwd in passwords:
                bloom.add(pwd)
    except FileNotFoundError:
        for pwd in default_passwords:
            bloom.add(pwd)
    
    return bloom

def main():
    MIN_ENTROPY = 30
    leaked_db = load_leaked_passwords()
    
    print("\nPassword Checker (enter 'quit' to exit)")
    
    while True:
        pwd = input("\nEnter password: ").strip()
        if not pwd or pwd.lower() == 'quit':
            break
        
        entropy = calculate_entropy(pwd)
        if pwd in leaked_db:
            print("✗ Breached password")
        elif entropy < MIN_ENTROPY:
            print(f"✗ Weak ({entropy:.1f} bits)")
        else:
            print(f"✓ Strong ({entropy:.1f} bits)")

if __name__ == "__main__":
    main()