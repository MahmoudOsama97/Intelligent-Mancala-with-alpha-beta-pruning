from utilities import show
def takePlayerMove(player,stealing,representation):
    while(1):
        p= int(input('\n which pocket do you want to move? '))

        if p>6 or p<1 :
            #print('Enter a valid pocket number')
            continue

        elif representation[player][p-1] == 0:
            #print('Enter a pocket that contains stones')
            continue

        else:
            side=player
            stones=representation[player][p-1]
            representation[player][p-1] = 0

        i=0
        position=p
        for i in range(stones):
            if position==6 and side!=player:
                side=player
                position=0

            if position==6 and side==player:
                representation[side][position]+=1
                if side==0:
                    side=1
                else:
                    side=0


            elif position<6 and position>=0:
                representation[side][position]+=1
            position=(position+1)%7
        if stealing==1:

            temp=6-position
            s=1-side
            if  representation[player][position-1]==1 and side==player and representation[s][temp]!=0:
                representation[player][6]=1+representation[s][temp]+representation[player][6]
                representation[side][position-1]=0
                representation[s][temp]=0
        if position==0 and side!=player and sum(representation[player][0:6]):
            show(representation)
            print("you will play again")
        else:
            break

    return representation

def takeAiMove(player,stealing,rep,p):
    playAgainFlag=0
    side=player
    stones=rep[player][p-1]
    rep[player][p-1] = 0

    i=0
    position=p
    for i in range(stones):
        if position==6 and side!=player:
            side=player
            position=0

        if position==6 and side==player:
            rep[side][position]+=1
            if side==0:
                side=1
            else:
                side=0


        elif position<6 and position>=0:
            rep[side][position]+=1
        position=(position+1)%7
    if stealing==1:

        temp=(6-position)
        s=1-side
        if  rep[player][position-1]==1 and side==player and rep[s][temp]!=0:
            rep[player][6]=1+rep[s][temp]+rep[player][6]
            rep[side][position-1]=0
            rep[s][temp]=0
    if position==0 and side!=player:
        playAgainFlag=1

    return rep,playAgainFlag
