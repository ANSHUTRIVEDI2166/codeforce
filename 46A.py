n = int(input())
pos = 1
res = []
for i in range(1, n):
    pos = (pos + i) % n
    if pos == 0:
        pos = n
    res.append(pos)
print(*res)
