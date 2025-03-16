n = int(input())
a = list(map(int, input().split()))

a.sort()
m = (n - 1) // 2
print(a[m])
