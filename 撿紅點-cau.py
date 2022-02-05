'''
這個函數是在執行分數計算
當遊戲結束後計算玩家與莊家所有卡牌的分數，分數大者即為優勝
在兩人的撿紅點遊戲當中，只有紅色卡牌有算分，A為20，9以上算10分
流程如下:
1.先算玩家手中的牌
2.算玩家計分堆裡的牌
3.算莊家手中的牌
4.算莊家中計分堆裡的牌
5.判別兩人分數大小，印出訊息
'''
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
