# 04 Поле чудес.

x = 0
y = 0
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
curr_dir = 1
step = input()

while step != 'СТОП':
    if step == 'шаг':
        x += directions[curr_dir][0]
        y += directions[curr_dir][1]
    elif step == 'направо':
        curr_dir = (curr_dir - 1) % 4
    elif step == 'налево':
        curr_dir = (curr_dir + 1) % 4

    step = input()

print(x, y)