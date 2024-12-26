import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number :
            print("Too low!")
        elif guess > random_number :
            print("Too high!")
    
    print (f"Yay, congrats!, You have a guessed the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    guess = 0
    while low <= high:
        guess = (low + high) // 2
        print(f"Is your number {guess} ?")
        response = input("Enter 'y' for yes, 'h' for high, 'l' for low: ")
        if response == 'y':
            print(f"I guessed it in {high - low + 1} attempts.")
            break
        elif response == 'l':
            low = guess + 1
        elif response == 'h':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'y', 'h', or 'l'.")


computer_guess(10)