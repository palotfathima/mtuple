
import random

print("LETS PLAY ROCK, PAPER, SCISSORS!\n")


while True:
    print("CHOOSE YOUR WEAPON!: \n 1 for ROCK, \n 2 for PAPER, \n 3 for SCISSOR \n")

    WEAPON = int(input("YOUR TURN: "))


    while WEAPON > 3 or WEAPON < 1:
        WEAPON = int(input("TRY AGAIN: "))


    if WEAPON == 1:
        CHOSEN_WEAPON = 'ROCK'
    elif WEAPON == 2:
        CHOSEN_WEAPON = 'PAPER'
    else:
        CHOSEN_WEAPON = 'SCISSOR'


    print("YOUR CHOICE IS: " + CHOSEN_WEAPON)
    print("\nNOW ITS THE COMPUTERS TURN!")


    COMPUTER = random.randint(1, 3)


    while COMPUTER == WEAPON:
        COMPUTER = random.randint(1, 3)


    if COMPUTER == 1:
        COMPUTER_WEAPON = 'ROCK'
    elif COMPUTER == 2:
        COMPUTER_WEAPON = 'PAPER'
    else:
        COMPUTER_WEAPON = 'SCISSOR'

    print("THE COMPUTER HAS CHOSEN: " + COMPUTER_WEAPON)

    print(CHOSEN_WEAPON + " V/S " + COMPUTER_WEAPON)


    if ((WEAPON == 1 and COMPUTER == 2) or
            (WEAPON == 2 and COMPUTER == 1)):
        print("PAPER WINS!", end="")
        result = "PAPER"

    elif ((WEAPON == 1 and COMPUTER == 3) or
          (WEAPON == 3 and COMPUTER == 1)):
        print("ROCK WINS!", end="")
        result = "ROCK"
    else:
        print("SCISSOR WINS!", end="")
        result = "SCISSOR"


    if result == CHOSEN_WEAPON:
        print("\nYOU HAVE WON! CONGRATULATIONS!")
    else:
        print("\nTHE COMPUTER HAS WON! BETTER LUCK NEXT TIME!")

    print("DO YOU WANT TO PLAY AGAIN? (YES/N0)")
    CHOICE = input()


    if CHOICE == 'NO' or CHOICE == 'no':
        break


print("\nTHANKS FOR PLAYING!")
