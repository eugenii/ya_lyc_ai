# 04 Вторые (максимумы).

first, second = -1000, -1000

while abs((number := int(input()))) < 1000:
    if number > first:
        second = first
        first = number
    elif number > second:
        second = number

print(second)