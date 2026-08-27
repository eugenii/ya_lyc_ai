from collections import defaultdict

birds = defaultdict(int)

while line := input():
    bird = line.split(': ')
    birds[bird[0]] += int(bird[1])

birds_dict = dict(birds)
print(birds_dict)

