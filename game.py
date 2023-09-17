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

# print(x)

for i in range(5):
    y = eval(input(f"請輸入一個數字{low}~{high}:"))
    if y == x:
        print("恭喜答對")
        break
        else:
            print("猜高一點")

            if y < high:
                high = y - 1
        else:
            print("猜高一點")
            if y > low:
                low = y + 1
>>>>>>> test

if y != x:
    print(f"答案為:{x}")


# 驗證是否包含最大數字
"""
while True:
    x = random.randint(low, high)
    print(x)
    if x == 50:
        break
"""
