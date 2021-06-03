from texttable import Texttable
import pickle

def initialize(representation):
  Player1 = [4, 4, 4, 4, 4, 4, 0]
  Player2 = [4, 4, 4, 4, 4, 4, 0]
  representation=[Player1,Player2]
  return representation

def show(representation):
    table = Texttable()
    table.header(["player 2","M2", "P6","P5","P4","P3","P2","P1" ,"M1"])
    table.add_row(["-",representation[1][6],representation[1][5],representation[1][4],representation[1][3],representation[1][2],representation[1][1],representation[1][0], "-"])
    table.add_row(["-","-" ,representation[0][0],representation[0][1],representation[0][2],representation[0][3],representation[0][4],representation[0][5],representation[0][6]])
    table.add_row(["player 1","M2", "P1","P2","P3","P4","P5","P6" ,"M1"])
    print(table.draw())

def save( path, data):
    try:
        with open(path+".pickle","wb") as f:
            pickle.dump(data,f)
    except Exception as e:
        print("couldn't save " , e)
def load(path):
    try:
        with open(path+".pickle","rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("couldn't load " , e)
