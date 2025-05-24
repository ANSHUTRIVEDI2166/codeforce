def solve():
    n = int(input())
    ans = [0] * (2 * n + 1)
    used = [False] * (2 * n + 1)
    
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            x = row[j - 1]
            ans[i + j] = x
            used[x] = True

    for i in range(1, 2 * n + 1):
        if ans[i] != 0:
            print(ans[i], end=' ')
        else:
            for j in range(1, 2 * n + 1):
                if not used[j]:
                    used[j] = True
                    print(j, end=' ')
                    break
    print()

t = int(input())
for _ in range(t):
    solve()
