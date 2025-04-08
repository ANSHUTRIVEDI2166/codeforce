def solve(k):
    if k % 2 != 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    k = int(input())
    solve(k)
