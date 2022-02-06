import random
def deal(gamercard):
    temp=card.pop()
    gamercard.append(temp)
def dealtable(gamerbox):
    temp=card.pop()
    tempoint=temp%13+1
    length=len(table)
    for i in table:
        tablepoint=i%13+1
        tablesuit=i//13
        if tempoint<10:
            if tempoint+tablepoint==10:
               gamerbox.append(i)
               gamerbox.append(temp)
               table.pop(table.index(i))
               break   
        else:
            if tempoint==tablepoint :
                gamerbox.append(i)
                gamerbox.append(temp)
                table.pop(table.index(i))
                break   
    if len(table)==length:
        table.append(temp)
def printmessage():
    print("*********************************************************")
    print("on table:",end=" ")
    printcard(table)
    print("playercard:",end=" ")
    printcard(playercard)
    
def printcard(gamercard):
    for i in gamercard:
        if i//13==0:
            print("\N{black diamond suit}",end="")
        elif i//13==1:
            print("\N{black heart suit}",end="")
        elif i//13==2:
            print("\N{black club suit}",end="")
        elif i//13==3:
            print("\N{black spade suit}",end="")
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
def cau():
    playerscore=0
    for i in playercard:
        psuit=i//13
        ppoint=i%13+1
        if psuit<2 and ppoint==1:
            playerscore+=20
        elif psuit<2 and 2<ppoint<9:
            playerscore+=ppoint
        elif psuit<2 and 9<=ppoint:
            playerscore+=10
    for i in playerbox:
        psuit=i//13
        ppoint=i%13+1
        if psuit<2 and ppoint==1:
            playerscore+=20
        elif psuit<2 and 2<ppoint<9:
            playerscore+=ppoint
        elif psuit<2 and 9<=ppoint:
            playerscore+=10
    print("玩家的分數:",playerscore)
    bankerscore=0
    for i in bankercard:
        bsuit=i//13
        bpoint=i%13+1
        if bsuit<2 and bpoint==1:
            bankerscore+=20
        elif bsuit<2 and 2<bpoint<9:
            bankerscore+=i
        elif bsuit<2 and 9<=bpoint:
            bankerscore+=10
    for i in bankerbox:
        bsuit=i//13
        bpoint=i%13+1
        if bsuit<2 and bpoint==1:
            bankerscore+=20
        elif bsuit<2 and 2<bpoint<9:
            bankerscore+=i
        elif bsuit<2 and 9<=bpoint:
            bankerscore+=10
    print("莊家的分數:",bankerscore)
    if playerscore>bankerscore:
        print("你贏了，恭喜你")
    else :
        print("嗚嗚嗚，再加油")
def check():
    for j in bankercard:
        for i in table:
            if j%13+1==9 and i%13+1==1 and i//13<2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
            elif (j%13+1)==(i%13+1) and (j%13+1)>9 and (i%13+1)>9 and i//13<2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
            elif (j%13+1)+(i%13+1)==10 and i//13<2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
    for j in bankercard:
        for i in table:
            if j%13+1==9 and i%13+1==1 and i//13>=2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
            elif (j%13+1)==(i%13+1) and (j%13+1)>9 and (i%13+1)>9 and i//13>=2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
            elif (j%13+1)+(i%13+1)==10 and i//13>=2:
                table.pop(table.index(i))
                bankercard.pop(bankercard.index(j))
                bankerbox.append(i)
                bankerbox.append(j)
                return
    temp=bankercard.pop()
    table.append(temp)
    return
card=list(range(0,52))
random.shuffle(card)
bankercard=list()
bankerbox=list()
playercard=list()
playerbox=list()
table=list()
for i in range (0,12):
    deal(bankercard)
    deal(playercard)
for i in range (0,5):
    deal(table)
while len(table)>0 and len(bankercard)>0:
    check()
    if len (table)>0:
        dealtable(bankerbox)
    printmessage()
    if len(table)>0 and len(playercard)>0:
        playersuit=input("請輸入你要出的花色:")
        if playersuit=="方塊":
            playersuit=0
        elif playersuit=="紅心":
            playersuit=1
        elif playersuit=="梅花":
            playersuit=2
        else :
            playersuit=3
        playerpoint=int(input("請輸入你要出的點數大小:"))
        temp=13*playersuit+playerpoint-1
        playercard.pop(playercard.index(temp))
        playerbox.append(temp)
        length=len(table)
        for i in table:
            tablepoint=i%13+1
            tablesuit=i//13
            if playerpoint<10:
                if playerpoint+tablepoint==10 and tablesuit<2:
                    playerbox.append(i)
                    table.pop(table.index(i))
                    break
                elif playerpoint+tablepoint==10 and tablesuit>=2:
                    playerbox.append(i)
                    table.pop(table.index(i))
                    break   
            else:
                if playerpoint==tablepoint and tablesuit<2:
                    playerbox.append(i)
                    table.pop(table.index(i))
                    break
                elif playerpoint==tablepoint and tablesuit>=2:
                    playerbox.append(i)
                    table.pop(table.index(i))
                    break
        if len(table)==length:
            table.append(temp)
        if len(table)>0:
            dealtable(playerbox)
    else:
        break
cau()
