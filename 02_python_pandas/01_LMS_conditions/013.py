mask = input()
if ('*' in mask or '?' in mask) and ' ' not in mask:
    print('Возможно маска')
else:
    print('Нет, это не маска!')