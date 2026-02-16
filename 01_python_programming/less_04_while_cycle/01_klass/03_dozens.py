# 03 Дюжины

amount = int(input())

while amount // 12 > 0:
    amount //= 12

print(amount)