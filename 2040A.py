for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [[] for _ in range(k)]
    for i in range(0, n):
        x = a[i]
        b[x % k].append(i + 1)
    res = -1
    for i in range(k):
        if len(b[i]) == 1:
            res = b[i][0]
            break
    if res == -1:
        print("NO")
    else:
        print("YES\n" + str(res))
