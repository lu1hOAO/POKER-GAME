# POKER-GAME
## 那些撲克牌小遊戲！
以前過年時我都會和表兄弟姊妹聚在一起玩一些撲克牌小遊戲(可惜都沒有賭錢，不然我應該賺不少)  
還有畢業旅行時，哪位同學有帶牌，晚上他的房間一定嗨翻天！  
可惜現在長大，過年回家的人越來越少，所以幫自己寫了一些卡牌小遊戲當作回味童年第二彈！！  
BTW我想時候最喜歡撿紅點，看日本電影夏日大作戰時，才發現原來撿紅點是從日本花札牌演變而來的！！(冷知識)
![起床2](https://user-images.githubusercontent.com/91367098/152663281-0b7ce3a5-2963-465a-a7ce-679766c4021b.png)
**********************************************************************************************************
21點的遊戲規則:  
一開始玩家有兩張牌，莊家只有一張，若玩家小於21點可以選擇加牌或不加，如果加完後超過21點，稱為爆牌，玩家就輸了
如果玩家選擇不加牌，且莊家小於17點，那系統自動幫莊家加牌，若遊戲結束兩人都沒爆牌點數大的為贏家   
![螢幕擷取畫面 (232)](https://user-images.githubusercontent.com/91367098/152663390-b7c07f1b-4ecd-4035-a832-a004e7b6fe26.png)
**********************************************************************************************************
撿紅點遊戲規則：
一開始玩家和莊家各有12張牌，桌上有4張牌，玩家和莊家要努力讓桌上的牌配對至無牌，配對規則如下:  
1.點數加起來十點  
2.超過十點兩張牌點數相等  
出牌配對成功後抽一張牌放在桌上，若抽出的牌可以和桌上牌配對那就讓他們配對(遵循配對原則)  
計分方式:  
只有紅色牌算分(方塊，紅心)，A為20，9 10 11 12 13為10分，其餘就是幾點得幾分(2點得兩分)  
超過105分者為勝！！  

![螢幕擷取畫面 (239)](https://user-images.githubusercontent.com/91367098/152663476-8511f04c-ff2c-410d-bcd7-d4faa6d07ab5.png)
**********************************************************************************************************
撿紅點電腦出牌的演算法  
雖然是只要點數有辦法配對就應優先出此牌，但只有紅牌有算分，為了確保最佳得分，判斷流程如下:
1.先找桌牌中紅色可配對的  
2.若無再找桌牌中黑色可配對的  
3.若前兩點都無，再隨機出一張黑牌
```.py
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
    for j in bankercard:
        if j//13>=2:
            bankercard.pop(bankercard.index(j))
            table.append(j)
            return
    temp=bankercard.pop()
    table.append(temp)
    return
    
