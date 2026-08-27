yes, no = 0, 0

while (answer := input()):
    if (answer == 'да'):
        yes += 1
    else:
        no += 1
if yes / (yes + no) >= 0.8:
    print('Достигли')
else:
    print('Пока нет')