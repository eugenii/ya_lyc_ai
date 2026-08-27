number = int(input())
res = 0
for i in range(1, int(number ** 0.5) + 1):
    if number % i == 0:
        res += i
        if i * i != number:
            res += number // i
print(res)