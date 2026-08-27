import sys
import io

# Важно: сделать ДО любых print
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

count = int(input())
for i in range(count):
    print(i + 1, input())
