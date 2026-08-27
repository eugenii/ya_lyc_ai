def line(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    if k == 0:
        k = 0.0
    if b > 0:
        print(f'y = {round(k, 2)} * x + {round(b, 2)}')
    else:
        print(f'y = {round(k, 2)} * x - {round(-b, 2)k}')