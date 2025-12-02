import random

def guess_number_game():
    number_to_guess = random.randint(1, 1000)
    attempts = 50
    print("You have 50 attempts to guess the number between 1 and 1000.")
    
    while attempts > 0:
        try:
            risposta = int(input("enter your guess:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        attempts -= 1 
        if risposta < 1 or risposta > 1000:
            print("Your guess is out of bounds. Please guess a number between 1 and 1000.")
            continue

        if risposta < number_to_guess:
            print("too low, you have", attempts, "attempts left")
        elif risposta > number_to_guess:
            print("too high", attempts, "attempts left")
        else:
            print(f"congratulations! You guessed the number in {50 - attempts} attempts!")
            break
            
    else:
        print("\nGAME OVER!")
        print(f"The number was: {number_to_guess}")

while True:
    print("welcome to the guess number game, you need to guess a number between 1 and 1000 " \
    "whit 50 attempts, for starting press 1 and for exit press 0")
    start = input("Enter your choice: ")
    if start == "1":
        guess_number_game()
    elif start == "0": 
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 0.")