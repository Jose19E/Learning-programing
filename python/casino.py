#Import libraries or packages
from random import randint
import os
#Declare and initialize variables and/or constants
lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
dices_addition = 0
status = True
player_lives = 3
acum_dices = 0

#Functons
def rollDices():
    dice1 = randint (1,6)
    dice2 = randint (1,6)
    return dice1, dice2



# Main
print(":::WELCOME TO CASINO:::")
press_key = input("\n::Press any key to start thre game::")
while status:
    os.system('cls')
    dices = rollDices()
    roll_count+=1
    dices_add=0
    print("#"*20)
    print(f"Roll dices N°.: {roll_count}")
    print("#"*20)
    print(f"Player lives: {player_lives}")

    if acum_dices > 14:
        dicex = dices[randint(0,1)]
        print(f"Dice: {dicex}")
        acum_dices += dicex
    else:
        print(f"Dice 1: {dices[0]}")
        print(f"Dice 2: {dices[1]}")
        dices_add= dices[0] + dices[1]
        acum_dices += dices_add

    if acum_dices >=20:
        print(":::CONGRATULATIONS, YOU WIN:::")
        break

    if dices_add % 2 != 0:
        player_lives-=1
        print(f"you´ve lost one live ::: Now you have {player_lives} lives")
        if player_lives == 0:
            print(":::GAME OVER:::")
            break
        

    if(dices [0] == 6 and dices[1] == 6) or (dices [0] == 1 and dices [1] == 1):
        player_lives+=1
        print(":::You´ve win one live:::")


    print(f"Dices addition (Current roll) {dices_add}")
    print(f"Dices acum: {acum_dices}")

    if player_lives == 0:
        print(":::GAME OVER)")
        print(f"Total Roll count: {roll_count}")
        break
    else:
        press_key = input("\nPress any key to roll dices again")

