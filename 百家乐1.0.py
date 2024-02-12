import random
Gold_Coin_Count = 10000

for i in range(0,100):
    Random_Number = random.randint(-1, 1)
    if Random_Number == 1:
        Gold_Coin_Count += 10
    elif Random_Number == 0:
        Gold_Coin_Count += 80
    else:
        Gold_Coin_Count == Gold_Coin_Count

print("玩家最后拥有:" + str(Gold_Coin_Count))