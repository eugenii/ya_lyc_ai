# 04 Концерты.
PRICE_A = 5000
PRICE_B = 3000
OTHER = 2000

concert_1, concert_2 = input(), input()

money = int(input()) * 1000

if concert_1 == concert_2:
    print("NOT TO GO")
elif concert_1 == "A" and concert_2 != "B":
    print((money - PRICE_A) // OTHER)
elif concert_1 == "B" and concert_2 != "A":
    print((money - PRICE_B) // OTHER)
elif concert_2 == "A" and concert_1 != "B":
    print((money - PRICE_A) // OTHER)
elif concert_2 == "B" and concert_1 != "A":
    print((money - PRICE_B) // OTHER)
else:
    print("NOT TO GO")
# print(concert_1, concert_2, money)