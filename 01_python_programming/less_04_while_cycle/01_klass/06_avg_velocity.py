# 06 Средняя скорость.

curr_sum = 0.0
count = 0

while (speed := float(input())):
    curr_sum += speed
    count += 1

print(curr_sum / count)