'''Number game
Outline:
Write a program to generate a random integer and 
match it with the input given by the user?

import random
playing = True
number = str(random.randint(10,20))

print("I will generate a number from 10 to 20, and you" 
" have to guess the number one digit at a time.")

print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best guess between 10-20:")
    if number== guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your guess insn't quite right, try again.")'''

'''Rock paper scissors
Outline:
Create a program to play rock, paper, and scissors.
Use a random module to select from the given options
Check whether the random guess matches the user’s answer

import random 

options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock,Paper or Scissors: ")

computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose",computer_choice)

if user_choice == computer_choice:
    print("Its a tie")

elif user_choice == "Rock" and computer_choice =="Scissors":
    print("Rock smashes scissors!You win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock!You win")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut paper!You win")
else:
    print("You lose!")'''



'''Mathematical operations
Outline:
Write a program to understand
the different functions of the math module.

import math
print(math.pow(17,24))

print(math.sqrt(81))

print(math.ceil(5.2))

print(math.floor(5.2))'''


