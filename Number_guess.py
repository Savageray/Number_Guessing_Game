#NUMBER GUESSING GAME
import random
from Number_guess_art import logo
print(logo)
print("Welcome to my random number guessing game. ")
random_number = random.randint(1,100)
print(f"FYI the number is {random_number}")
decision = input("Choose the difficulty of the game, either 'easy' or 'hard'\n").lower()
if decision == 'easy':
    lives = 10
elif decision== 'hard':
    lives = 5
else:
    print("Invalid choice, defaulting to easy.")
    lives = 10
print(f"You have {lives} lives, all the best.")
while lives >0 :
    guess = int(input("Guess a number between 1 and 100: \n"))
    if guess == random_number:
         print(f"You got it right 🎉. The answer was {random_number}")
         play_again = input(f"Do you want to play again?Choose 'y' to continue or 'n' to quit. \n")
         if play_again == 'y':
             random_number = random.randint(1, 100)
             decision = input("Choose the difficulty of the game, either 'easy' or 'hard'\n").lower()
             if decision == 'easy':
                 lives = 10
             elif decision == 'hard':
                 lives = 5
             else:
                 print("Invalid choice, defaulting to easy.")
                 lives = 10
             print(f"You have {lives} lives, all the best.")
             continue
         else:
             print(f"Thanks for playing. Goodbye.")
             break
    elif guess < random_number:

        print("Too low my friend, try again. ")
    else:
        print("Too high my friend, try again. ")
    lives -= 1

    if lives >0:
        print(f"Oops!! Wrong guess. You have {lives} left.")
    else:
        print(f"💀  Yikes!! It appears your lives are depleted. The number was {random_number}\n GAME OVER!!!!")
        play_again = input(f"Do you want to play again?Choose 'y' to continue or 'n' to quit. \n")
        if play_again == 'y':
            random_number = random.randint(1, 100)
            decision = input("Choose the difficulty of the game, either 'easy' or 'hard'\n").lower()
            if decision == 'easy':
                lives = 10
            elif decision == 'hard':
                lives = 5
            else:
                print("Invalid choice, defaulting to easy.")
                lives = 10
            print(f"You have {lives} lives, all the best.")
            continue
        else:
            print(f"Thanks for playing. Goodbye.")
            break
