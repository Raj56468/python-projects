import random 


def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_chars = "0123456789"
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"


    all_chars = lowercase_chars
    if use_uppercase:
        all_chars += uppercase_chars
    if use_numbers:
        all_chars += number_chars
    if use_special_chars:
        all_chars += special_chars

        if len(all_chars) == 0:
            raise ValueError("Invalid password length or character set")

    password = random.choices(all_chars, k= length)
    return ''.join(password)

if __name__ == "__main__":
    length =  int(input("Enter password length (default 12): ") or 12)
    uppercase = input("Include uppercase letters? (y/n): ").lower() != 'n'
    numbers = input("Include numbers? (y/n): ").lower() != 'n'
    special_chars = input("Include special characters? (y/n): ").lower() != 'n'

    password = generate_password(length, uppercase, numbers, special_chars)
    print(f"Generated password: {password}")