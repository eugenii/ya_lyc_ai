first, second = False, False

phrases = []

while phrase := input():
    if not first:
        if 'Все хорошо' not in phrase:
            continue
        first = True
        continue
    if 'Все хорошо' in phrase:
        break
    phrases.append(phrase)

for phrase in reversed(phrases):
    print(phrase)
