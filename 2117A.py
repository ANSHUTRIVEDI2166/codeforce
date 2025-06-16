import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
res = []
for _ in range(t):
    n, x = data[idx], data[idx + 1]
    idx += 2
    l, r = 10**9, -1
    for i in range(n):
        door = data[idx + i]
        if door == 1:
            l = min(l, i)
            r = max(r, i)
    idx += n
    res.append("YES" if x >= r - l + 1 else "NO")
print("\n".join(res))
