"""
猜數字遊戲
1.要可以任意產生亂數(1~50)
2.使用者可以猜數字
3.比對是否猜對
4.可以多次猜測
5.
"""
import random

low, high = 1, 50
x = random.randint(low, high)

print(x)

y = eval(input(f"請輸入一個數字{low}~{high}:"))

if y == x:
    print("恭喜答對")
else:
    print("答錯")


# 驗證最大數字是否包含
"""
while True:
    x = random.randint(low, high)
    print(x)
    if x == 50:
        break
"""
