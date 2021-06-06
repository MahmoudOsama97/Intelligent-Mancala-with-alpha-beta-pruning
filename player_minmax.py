import copy
from move import takeAiMove
class Player:
    def __init__(self, num,mode):
        self.num = num
        self.mode=mode

    def isGameOver(self,rep):
        return sum(rep[1][0:6])==0 or sum(rep[0][0:6])==0

    def EvalFn(self,rep):
        #(rep[self.num][6]-rep[1-self.num][6]) + 0.5
        #if self.maxOrMin==1:
        return (rep[self.num][6]-rep[1-self.num][6])
        #else:
            #return (rep[1-self.num][6]- rep[self.num][6]) #-sum(rep[self.num][3:6])-sum(rep[1-self.num][0:3])
    def minimax(self,rep, depth, alpha, beta, maximizingPlayer):
        #print(depth)
        if depth == 0 or self.isGameOver(rep)==True:
            #print("here  {},,,, {}".format(depth,self.isGameOver(rep)))
            return self.EvalFn(rep),0
        tempRep = copy.deepcopy(rep)
        if maximizingPlayer==True:
            maxEval = -1000
            i=1
            move=0
            while(i>=1 and i<=6):
                if rep[self.num][i-1]==0:
                    i+=1
                    continue
                tempRep,playAgainFlag=takeAiMove(self.num,self.mode,tempRep,i)
                if playAgainFlag==0:
                    eval,_ = self.minimax(tempRep, depth - 1, alpha, beta, False)
                else:
                    eval,_ = self.minimax(tempRep, depth - 1, alpha, beta, True)


                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)

                if alpha==eval:
                    move=i
                if beta <= alpha:
                    break

                i+=1
            return maxEval,move

        else:
            minEval = +1000
            move=0
            i=1
            while(i>=1 and i<=6):
                if rep[1-self.num][i-1]==0:
                    i+=1
                    continue
                tempRep,playAgainFlag=takeAiMove(1-self.num,self.mode,tempRep,i)
                if playAgainFlag==0:
                    eval,_ = self.minimax(tempRep, depth - 1, alpha, beta, True)
                else:
                    eval,_ = self.minimax(tempRep, depth - 1, alpha, beta, False)


                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta==eval:
                    move=i
                if beta <= alpha:
                    break
                i+=1
            return minEval,move
