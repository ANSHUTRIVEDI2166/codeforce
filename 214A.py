n, m = map(int, input().split())
count = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i * i + j == n and i + j * j == m:
            count += 1

print(count)
