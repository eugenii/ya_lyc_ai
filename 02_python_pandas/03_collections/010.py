fishes = {}
while fish := input():
    cur_fish, height = fish.split()
    if cur_fish not in fishes:
        fishes[cur_fish] = (int(height), int(height))
    else:
        fishes[cur_fish] = (
            min(fishes[cur_fish][0], int(height)),
            max(fishes[cur_fish][1], int(height)),
        )
print(fishes)