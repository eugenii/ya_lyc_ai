count = 0
while (number := float(input())) < 36.6:
    if number < 0:
        count += 1
print(count)