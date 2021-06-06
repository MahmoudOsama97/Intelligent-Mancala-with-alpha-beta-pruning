from utilities import *
from move import takeAiMove, takePlayerMove
import numpy as np
from player_minmax import Player

def main():
    playAgain=1
    while(playAgain):
        newGame=int(input("Do you want to start new game or continue ? (0:continue, 1:new): "))

        if newGame==1:
            Player1 = [4, 4, 4, 4, 4, 4, 0]
            Player2 = [4, 4, 4, 4, 4, 4, 0]
            representation=[Player1,Player2]
        else:
            path=input("Enter loading file name: " )
            representation=load(path)


        savingMode=int(input("Do you want to save your game status while playing ? (0:No, 1:Yes): " ))
        if savingMode:
            savingPath=input("Enter saving file name: " )
        stealing =int(input("Enter mode (0:Without Stealing, 1:With Stealing): " ))
        player=0
        playAgainFlag=0
        Ai1=Player(1,stealing)
        Ai0=Player(0,stealing)

        #game types
        print("Choose The Game Type: ")
        print("1- Player vs Player")
        print("2- Player vs AI")
        print("3- AI vs Player")
        print("4- AI vs AI")
        game=int(input("Game Type: "))
        if game==2 or game==3:
            difficulty1=int(input("Enter AI difficulty(1-12): "))
        elif game==4:
            difficulty1=int(input("Enter AI1 difficulty(1-12): "))
            difficulty2=int(input("Enter AI2 difficulty(1-12): "))

        show(representation)
        while(1):

            print('Player {} Move'.format(player+1))
            if game==1:
                if player==0:
                    representation=takePlayerMove(player,stealing,representation)

                else:
                    representation=takePlayerMove(player,stealing,representation)
            elif game==2:
                if player==0:
                    representation=takePlayerMove(player,stealing,representation)

                else:
                    val,p=Ai1.minimax(representation, difficulty1, -1000, 1000, True)
                    print(p)
                    representation,playAgainFlag=takeAiMove(player,stealing,representation,p)

            elif game==3:
                if player==0:
                    val,p=Ai0.minimax(representation, difficulty1, -1000, 1000, True)
                    print(p)
                    representation,playAgainFlag=takeAiMove(player,stealing,representation,p)
                else:

                    representation=takePlayerMove(player,stealing,representation)
            elif game==4:
                if player==0:
                    val,p=Ai0.minimax(representation, difficulty1, -1000, 1000, True)
                    print(p)
                    representation,playAgainFlag=takeAiMove(player,stealing,representation,p)
                else:
                    val,p=Ai1.minimax(representation, difficulty2, -1000, 1000, True)
                    print(p)
                    representation,playAgainFlag=takeAiMove(player,stealing,representation,p)


            if playAgainFlag!=1:
                playAgainFlag=0
                player=1-player
            if sum(representation[0][0:6])==0 or sum(representation[1][0:6])==0:
                print("Game Over")
                representation[0][6]=sum(representation[0][0:7])
                representation[1][6]=sum(representation[1][0:7])
                Player1 = [0, 0, 0, 0, 0, 0, representation[0][6]]
                Player2 = [0, 0, 0, 0, 0, 0, representation[1][6]]
                representation=[Player1,Player2]
                if representation[0][6]>representation[1][6]:
                    print("player 1 wins")
                elif representation[0][6]<representation[1][6]:
                    print("player 2 wins")
                else:
                    print("Draw")
                show(representation)
                save(savingPath,representation)
                break

            show(representation)
            if savingMode==1 and player==0:
                save(savingPath,representation)

        playAgain=int(input("Do you want to play again? (yes:1, no:0): " ))

if __name__ == '__main__':
    main()
