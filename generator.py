import random
import string

def generate_password(length):
    # Define the character set from which to generate the password
    characters = string.ascii_letters  # includes both uppercase and lowercase letters
    
    # Generate a password of specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage:
password_length = 10  # You can adjust the length as needed
password = generate_password(password_length)
print("Generated Password:", password)
