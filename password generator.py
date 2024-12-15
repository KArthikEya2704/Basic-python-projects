import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    
    if length < 4:
        return "Error: Password length should be at least 4 characters."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''
    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        return "Error: No character types selected for the password."

    
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))
    while len(password) < length:
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print('''Welcome to karthikeya's Password Generator!''')
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for the password length.")
