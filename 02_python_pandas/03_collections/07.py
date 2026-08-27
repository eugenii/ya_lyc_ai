count = int(input())
children = {input(): 0 for _ in range(count)}

for _ in range(int(input())):
    name = input()
    if children[name] == 1:
        print(f'{name}, всем по одному подарку!')
    else:
        print(f'Вот твой подарок, {name}!')
        children[name] += 1