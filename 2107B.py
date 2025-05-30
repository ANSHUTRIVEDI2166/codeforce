t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)

    a.sort()
    a[-1] -= 1
    a.sort()

    if a[-1] - a[0] > k or total % 2 == 0:
        print("Jerry")
    else:
        print("Tom")
