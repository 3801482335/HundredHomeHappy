import random
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

Gold_Coin_Count = 100000
zhuang = 1
he = 0
xian = -1
Player_buy = zhuang

while True:
    invest = 10
    Gold_Coin_Count -= invest
    while True:
        Gome_Buy = random.randint(1, 100)

        if 1 <= Gome_Buy and Gome_Buy <= 46:
            Gome_Buy = 1
        elif 47 <= Gome_Buy and Gome_Buy <= 92:
            Gome_Buy = -1
        else:
            Gome_Buy = 0

        if Player_buy == zhuang and Gome_Buy == 1:
            Gold_Coin_Count += invest*(1-6/100)
        elif Player_buy == zhuang and (Gome_Buy == 0 or Gome_Buy == -1):
            Gold_Coin_Count -= invest
        if Gome_Buy == 0 or Gome_Buy == -1:
            invest *= 2
        if Gold_Coin_Count < invest:
            break
    if Gold_Coin_Count < invest:
        break
    print("玩家爆仓！")
money = decimal.Decimal(Gold_Coin_Count)

print("玩家最后拥有:",round(money,2))
if Gold_Coin_Count > 100000:
    print("玩家最后赚了: ",round(money,2) - 100000)
else:
    print("玩家最后亏了: ",100000 - round(money, 2))