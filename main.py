from math import *
import random
import os

player1Score = 0
player2Score = 0

player1Roll = 0
player2Roll = 0

def diceRoll() :

    global player1Score
    global player2Score
    global player1Roll
    global player2Roll

    player1Roll = int(player1Roll)
    player2Roll = int(player2Roll)

    player1Roll = random.randint(1, 6)
    player2Roll = random.randint(1, 6)

    input("Press enter to roll the dice!")

    os.system('cls')

    if(player1Roll != 1 and player2Roll != 1) :
        
        if(player1Roll == player2Roll) :

            print("Both players rolled",  player1Roll, "however neither got a one, so the game continues!")

            diceRoll()

        player1Score = int(player1Score)
        player2Score = int(player2Score)

        print("The first player rolled ",  player1Roll, " and the second player rolled ",  player2Roll, "!")

        diceRoll()

    if(player1Roll == 1 and player2Roll == 1) :
        print("Both players rolled a 1, it's a draw! how unlikely!")

        input("Press enter to play again.")
        os.system('cls')

    if(player1Roll == 1) :
        
        player1Score = int(player1Score)

        player1Score += 1

        print("The first player rolled a 1 and has therefore won a point.")
        print("Player 1 score :", player1Score)
        print("Player 2 score :", player2Score)

        if(player1Score == 10 or player2Score == 10):
            if(player1Score == 10):
                print("The first player has reached the score of 10 and therefore wins!")
                input("Press enter to start over (scores will be reset).")

                player1Score = 0
                player2Score = 0
            elif(player2Score == 10):
                print("The second player has reached the score of 10 and therefore wins!")
                input("Press enter to start over (scores will be reset).")

                player1Score = 0
                player2Score = 0
            diceRoll()

        input("Press enter to play again.")

        os.system('cls')

    if(player2Roll == 1) :

        player2Score = int(player2Score)

        player2Score += 1

        player1Score = str(player1Score)
        player2Score = str(player2Score)

        print("The second player rolled a 1 and has therefore won a point.")
        print("Player 1 score : ", player1Score)
        print("Player 2 score : ", player2Score)

        player1Score = int(player1Score)
        player2Score = int(player2Score)

        if(player1Score == 10 or player2Score == 10):
            if(player1Score >= 10):
                print("The first player has reached the score of 10 and therefore wins!")
                input("Press enter to start over (scores will be reset).")

                player1Score = 0
                player2Score = 0
            elif(player2Score == 10):
                print("The second player has reached the score of 10 and therefore wins!")
                input("Press enter to start over (scores will be reset).")

                player1Score = 0
                player2Score = 0
            gameStart()

        input("Press enter to play again.")

        os.system('cls')
    
    diceRoll()

def gameStart() :

    os.system('cls')
    input("Press enter to start playing!")
    os.system('cls')
    diceRoll()
    
gameStart()