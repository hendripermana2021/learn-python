import random

def main():
    user = input("Please choice you want, r for rock, s for scissors, and p for paper? : ")
    computer = random.choice(['r', 's', 'p'])


    if (user == computer):
        print("It's a tie!")
        print("Computer choice: ", computer)

    if(user != "r" and "s" and "p"):
        print("Invalid input! Please enter r, s, or p.")
    
    if is_win(user, computer):
        print("Computer choice: ", computer)
        print("You win!")
    
    return "you lost!" 

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    else:
        return False
    

main()