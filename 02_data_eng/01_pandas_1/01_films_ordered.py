# films ordered

count = int(input())
films = [input() for _ in range(count)]
films_ordered = sorted(films)
result = films_ordered[:3] + films_ordered[-3:]
print(*result, sep="\n")