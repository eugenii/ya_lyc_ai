data = []
count = int(input())
sum_raiting = 0
for i in range(count):
    # data.append(input().encode('cp1251').decode('utf-8').split(";"))
    data.append(input().split(";"))
    sum_raiting += float(data[-1][1])
avg_raiting = sum_raiting / count
result = [film[0] for film in data if float(film[1]) > avg_raiting]
print("{:.3f}".format(avg_raiting))
if result:
    print(*result, sep="\n")
