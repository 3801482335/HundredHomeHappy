import random
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

Gold_Coin_Count = 100000
b = 0
zhuang = 1
he = 0
xian = -1
Player_buy = zhuang
while b < 10000:#玩家最多玩一万局
    while True:#玩家胜出，继续从10元开始下注
        invest = 10
        Gold_Coin_Count -= invest
        while True:#如果上一局游戏失败，马丁策略下注下一局
            b += 1
            Game_Buy = random.randint(1, 100)

            if 1 <= Game_Buy and Game_Buy <= 46:
                Game_Buy = 1
            elif 47 <= Game_Buy and Game_Buy <= 92:
                Game_Buy = -1
            else:
                Game_Buy = 0

            if Player_buy == zhuang and Game_Buy == 1:
                Gold_Coin_Count += invest*(2-6/100)
                break
            if Player_buy == zhuang and (Game_Buy == 0 or Game_Buy == -1):
                invest *= 2
            if Gold_Coin_Count < invest or b >= 10000:
                break
        if Gold_Coin_Count < invest:
            print("玩家爆仓！")
            break
        elif b >= 10000:
            print("已到10000局！游戏结束！")
            break

money = decimal.Decimal(Gold_Coin_Count)

print("玩家最后拥有:",round(money,2))
if Gold_Coin_Count > 100000:
    print("玩家最后赚了: ",round(money,2) - 100000)
else:
    print("玩家最后亏了: ",100000 - round(money, 2))
print("玩家一共玩了" + str(b) + "局")