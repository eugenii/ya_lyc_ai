elts = []
while elt := int(input()):
    elts.append(elt)
n = len(elts)
res = [i for i in elts if i % n == 0]
print(res)
