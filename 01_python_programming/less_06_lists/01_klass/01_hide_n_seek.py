# 01 Прятки.

count = int(input())
lines = []
for i in range(count):
    lines.append(input())

count = int(input())
for i in range(count):
    name = input()
    for i in range(len(lines)):
        if name in lines[i]:
            print(i + 1)
            break
    else:
        print(-1)
