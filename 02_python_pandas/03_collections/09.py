count = int(input())

sertificates = {}
for _ in range(count):
    grade = input().split()
    sertificates[grade[0]] = (int(grade[1]), int(grade[2]))

points = sum([int(i) for i in input().split()])

for grade in sertificates:
    if points in range(sertificates[grade][0], sertificates[grade][-1] + 1):
        print(grade)
        break