# Календарь Хааб

num = int(input())

if num > 360:
    print(f"Месяц {19}, день {num - 360 - 1}.")
elif num == 0:
    print(f"Месяц {1}, день {0}.")
else:
    month = num // 19 + 1 if num % 19 != 0 else num // 19
    day = num - (month - 1) * 19 - 1
    # print(f"Месяц {month}, день {day}.")

    print(f"Месяц {month}, день {day}.")