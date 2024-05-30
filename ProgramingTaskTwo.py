import random


def guess_number():
    # Generate a random number
    number = random.randint(1, 100)
    # A boolean flag to control while loop
    flag = True
    while flag:
        user_guess = input("Please enter a number between 1 and 100: ")
        if valid_user_input(user_guess):
            user_guess = int(user_guess)
            if valid_number(user_guess):
                if user_guess < number:
                    print("Lower")
                elif user_guess > number:
                    print("Higher")
                else:
                    print("Correct")
                    flag = False
        else:
            print("Please enter a valid number between 1 and 100.")


# Validation if user input is a number
def valid_user_input(user_enter):
    if user_enter.isdigit():
        return True
    else:
        return False


# Validation if user input number is in the range
def valid_number(user_enter):
    if user_enter < 1 or user_enter > 100:
        return False
    else:
        return True


if __name__ == '__main__':
    guess_number()
