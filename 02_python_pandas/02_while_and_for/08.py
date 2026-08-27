first, second = None, None
res = 0
while vel := int(input()):
    if not first:
        first = vel
        continue
    second = vel
    if second > first:
        res += 1
    first = second
print(res)