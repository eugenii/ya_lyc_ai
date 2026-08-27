n, m = int(input()), int(input())
out = ''
for i in range(n, 32, m):
    out += str(i) + ' '
print(out.strip())