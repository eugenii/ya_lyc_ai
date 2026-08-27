count = int(input())
strings = [input() for i in range(count)]

count = int(input())
for i in range(count):
    name = input()
    for i in range(len(strings)):
        if name in strings[i]:
            print(i + 1)
            break
    else:
        print(-1)