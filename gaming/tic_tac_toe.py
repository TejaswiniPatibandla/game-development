def printBoard(xSate,zState):
    zero='X' if xState[0]else ('$' if zState[0] else 0)
    one='X' if xState[1]else ('$' if zState[1] else 1)
    two='X' if xState[2]else ('$' if zState[2] else 2)
    three='X' if xState[3]else ('$' if zState[3] else 3)
    four='X' if xState[4]else ('$' if zState[4] else 4)
    five='X' if xState[5]else ('$' if zState[5] else 5)
    six='X' if xState[6]else ('$' if zState[6] else 6)
    seven='X' if xState[7]else ('$' if zState[7] else 7)
    eight='X' if xState[8]else ('$' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"----------")
    print(f"{three} | {four} | {five} ")
    print(f"----------")
    print(f"{six} | {seven} | {eight} ")
    print(f"----------")
    pass

def sum(a,b,c):
    return a+b+c

def win(xState,zState):
    wins=[[0,1,2],[0,3,6],[0,4,8],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("X wins")
            return 1
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            print("$ wins ")
            return 0
    return -1
if __name__=="__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 #1forx and o for O

    print("tic-tac-toe")
    while(True):
        printBoard(xState,zState)
        if(turn==1):
            print("X's chance")
            value=int(input("please enter a value"))
            xState[value]=1
        else:
            print("$'s chance")
            value=int(input("please enter a value"))
            zState[value]=1
        ww=win(xState,zState)
        if(ww!=-1):
            print("match over")
            break

        turn=1-turn

        
