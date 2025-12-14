import random

r = random.randint(1, 100)

def guess_number(user_guess):
    if user_guess < r:
        return "Too low!"
    elif user_guess > r:
        return "Too high!"
    else:
        return "Correct! You've guessed the number."

try:
    user_input = int(input("Guess a number between 1 and 100: "))
    result = guess_number(user_input)
    print(result)

except ValueError:
    print("Please enter a valid integer.")