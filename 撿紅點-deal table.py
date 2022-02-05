'''
這個函數是在執行玩家出玩牌後從牌堆抽出一張排放到桌上的過程:
如果抽出的牌和原本桌上的牌能配對，就必須湊成一對放到玩家的計分牌當中
若無法湊成一對，就必須放在桌上
流程如下:
1.先從牌堆抽出一張牌儲存於temp
2.依temp的屬性判別是否和桌上的牌湊成堆
'''
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
        else:
            if tempoint==tablepoint :
                gamerbox.append(i)
                gamerbox.append(temp)
                table.pop(table.index(i))   
    if len(table)==length:
        table.append(temp)
