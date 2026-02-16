# Пикник.

number = int(input())
divider = 1
while divider != number + 1:
    if number % divider == 0:
        print(divider)
    divider += 1
