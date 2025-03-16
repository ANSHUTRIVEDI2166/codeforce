n = int(input())
x = 0
c = 0
i = 1

while x + i * (i + 1) // 2 <= n:
    x += i * (i + 1) // 2
    c += 1
    i += 1

print(c)
