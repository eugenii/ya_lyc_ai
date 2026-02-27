# 02 Только кратные.

data = []
while num := int(input()):
    data.append(num)

result = []
length = len(data)

for element in data:
    if element % length == 0:
        result.append(element)

print(result)