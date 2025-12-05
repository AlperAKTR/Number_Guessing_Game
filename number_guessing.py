from random import randint

def text_input(prompt, allowed_answers=None):
    """
    Safely asks the user for text input.
    - Ensures the input contains only alphabetic characters.
    - If allowed_answers is provided, input must match one of them.
    """
    while True:
        answer = input(prompt).lower().strip()

        if not answer.isalpha():
            print("Please enter a valid text input!")
            continue

        if allowed_answers and answer not in allowed_answers:
            print(f"Please enter only: {', '.join(allowed_answers)}")
            continue

        return answer


def main():
    print("Welcome to the Number Guessing Game!")
    print("I will think of a number between 1 and 50, and your job is to guess it!")

    start = text_input("Do you want to play? (y/n): ", allowed_answers=["y", "n"])

    attempts = 0

    if start == "y":
        random_number = randint(1, 50)
        print("Great! Let's begin. I've chosen my number.")

        guess = 0

        while guess != random_number:
            try:
                guess = int(input("Enter your guess (1-50): "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            attempts += 1

            if guess > random_number:
                print("Too high!")
            elif guess < random_number:
                print("Too low!")
            else:
                print(f"Correct! The number was {random_number}.")
                print(f"You guessed it in {attempts} attempts.")

        play_again = text_input("Do you want to play again? (y/n): ", allowed_answers=["y", "n"])

        if play_again == "n":
            print("Thanks for playing! See you next time.")

    else:
        print("Maybe another time!")



if __name__ == "__main__":
    main()
