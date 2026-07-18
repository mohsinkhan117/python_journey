import random

random_number = random.randint(1, 5)  
guess = int(input('Enter a guess: '))

while True:
    if guess == random_number:
        print("You win!")
        break  

    print(f"You lose, the number is: {random_number}")
    
    choice = input("Try again? (y/n): ").lower()
    if choice == 'n' :
        print("Game exited.")
        break  

    guess = int(input('Enter a guess: '))