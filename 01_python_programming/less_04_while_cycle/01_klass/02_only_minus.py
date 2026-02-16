# 02 Только минус. 

count = 0

while (temperature := float(input())) <= 36.3:
    if temperature < 0:
        count += 1

print(count)