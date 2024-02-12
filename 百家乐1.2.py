import random
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

Gold_Coin_Count = 100000
zhuang = 1
he = 0
xian = -1
Player_buy = zhuang
formerly = 100000
a = 10/100*6

while True:
    invest = 10
    Gold_Coin_Count -= invest
    for i in range(0, 100):
        Gome_Buy = random.randint(1, 100)

        if 1 <= Gome_Buy <= 45:
            Gome_Buy = 0
        elif 47 <= Gome_Buy <= 91:
            Gome_Buy = -1
        else:
            Gome_Buy = 1

        if Player_buy == zhuang and Gome_Buy == 1:
            Gold_Coin_Count += 10- a
        elif Player_buy == zhuang and (Gome_Buy == 0 or Gome_Buy == -1):
            Gold_Coin_Count -= 10
    if Gold_Coin_Count < formerly:
        invest *= 2
    if Gold_Coin_Count > formerly or Gold_Coin_Count < invest:
        break
money = decimal.Decimal(Gold_Coin_Count)

print("玩家最后拥有:",round(money,2))
print("玩家最后赚了: ",round(money,2) - 100000)