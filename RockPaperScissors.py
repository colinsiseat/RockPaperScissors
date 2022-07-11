#bot

import random

#rock = 1
#paper = 2
#scissors = 3
botty = random.randrange(1,3)

startgame= input("Would you like to play! \n")

person = input("what will you choose? Type 1 for rock, 2 for paper, or 3 for scissors! \n")






if startgame == "yes":
     if person == "1":
        if botty == 1:
            print("It's a tie!!")
        if botty == 2:
            print("I win!!")
        if botty == 3:
            print("You won!:(")

     if person == "2":
            if botty == 1:
                print("You won!:(")
            if botty == 2:
                print("It's a tie!!")
            if botty == 3:
                print("I won!!")
     if person == "3":
          if botty == 1:
             print("I win!!!!")
          if botty == 2:
             print("You won!:(")
          if botty == 3:
             print("It's a tie!!")

if startgame == "no":
    exit()




    


    
    