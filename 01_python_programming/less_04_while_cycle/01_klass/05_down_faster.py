# Быстрее вниз.

count = 0
last = 0
while (number := int(input())):
    if last == 0:
        last = number
    elif number > last:
        count += 1
    last = number

print(count)