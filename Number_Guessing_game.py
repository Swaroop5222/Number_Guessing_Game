#Number_Guessing_Game
'''
Guess the Correct number until it's true
'''

import random

print("This is a Number Guessing Game.")
print("You have to guess a number between 1-100. If it matches with the number choosen by the computer then you are winner")
while(True):
    ask=input("Do you wanna play the game?(y/n): ")
    num2=random.randint(1,100)
    count=0
    if ask=='y':
        while(True):
            num1=int(input("Enter number(1-100): "))
            if num1<=100:
               count+=1
               if num1<num2:
                print("Too low!")
                continue
               elif num1>num2:
                print("Too high!")
                continue
               else:
                print("Yes you guessed correct number")
                print("You took",count," attempts to guess the correct number")
                break
            else:
              print("Enter number between 1 to 100 only!")
    elif ask=='n':
      break
    else:
        print("Enter either 'y' or 'n' to continue")
print("Game Completed.Hope you enjoyed")
    