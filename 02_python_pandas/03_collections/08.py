dreams = []

while len(dream := input()):
    dreams.append(dream)

start, end = int(input()), int(input())

max_len_dream = max(dreams[start - 1: end], key=len)
print(max_len_dream)

