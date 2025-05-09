t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = a[0]
    for i in range(1, n):
        res = (res + a[i]) // 2
    print(res)
