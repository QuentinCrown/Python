import random

def main():
    # random number between 1 and 100
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

    while True:
        try:
            # guess in terminal
            guess = int(input("Enter your guess: "))

            # is guess correct
            if guess == number:
                print("Congratulations! You guessed the correct number.")
                break

            # how close is your number
            difference = abs(guess - number)

            # hot or cold
            if difference <= 5:
                print("Very Hot!")
            elif difference <= 15:
                print("Hot!")
            elif difference <= 25:
                print("Cool!")
            else:
                print("Cold!")

        except ValueError:
            # must be number
            print("Invalid input! Please enter a number.")

# main
if __name__ == "__main__":
    main()
