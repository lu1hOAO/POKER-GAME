import random
def deal(gamercard,gamerpoint):
    temp=card.pop()
    gamercard.append(temp)
    if temp%13==0:
        gamerpoint.append(11)
    elif temp%13>10:
        gamerpoint.append(10)
    else:
        gamerpoint.append(temp%13+1)
    
def printmessage():
    print("玩家的牌:",end="")
    printcard(playercard)
    print("玩家的牌面點數：",sum(playerpoint))
    print("莊家的牌:",end="")
    printcard(bankercard)
    print("莊家的牌面點數:",sum(bankerpoint))    
    print("****************************************")
def printcard(c):
    for i in c:
        if i//13==0:
            print("\N{black spade suit}",end="")
        elif i//13==1:
            print("\N{black heart suit}",end="")
        elif i//13==2:
            print("\N{black diamond suit}",end="")
        elif i//13==3:
            print("\N{black club suit}",end="")
        if i%13==0:
            print("A",end=" ")
        elif i%13==10:
            print("J",end=" ")
        elif i%13==11:
            print("Q",end=" ")
        elif i%13==12:
            print("K",end=" ")
        else:
            print(i%13+1,end=" ")
    print()
#主程式開始
card=list(range(0,52))
random.shuffle(card)
playercard=list()
playerpoint=list()
bankercard=list()
bankerpoint=list()
for i in range (2):
    deal(playercard,playerpoint)
deal(bankercard,bankerpoint)
printmessage()
while True:
    ans=input("玩家是否要加牌(y/n):")
    if ans=='N' or ans=='n':
        break
    deal(playercard,playerpoint)
    if sum(playerpoint)>21:
        if 11 in playerpoint:
           playerpoint[playerpoint.index(11)]=1
           printmessage()
        else :
            printmessage()
            print("玩家爆牌，莊家獲勝，嘿嘿嘿")
            break
    else :
        printmessage()
if sum(playerpoint)<22:
    while sum(bankerpoint)<17:
        deal(bankercard,bankerpoint)
        if sum(bankerpoint)>21:
            if 11 in playerpoint:
                bankerpoint[bankerpoint.index(11)]=1
                printmessage()
            else :
                printmessage()
                print("莊家爆牌，玩家獲勝,恭喜你!")
                break
        else :
            printmessage()
    if 17<=sum(bankerpoint)<21:
        if sum(playerpoint)>sum(bankerpoint):
            print("玩家獲勝，恭喜喔！")
        elif sum(playerpoint)==sum(bankerpoint):
            print("兩人平手耶")
        else :
            print("莊家獲勝，嘿嘿嘿")