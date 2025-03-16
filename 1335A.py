def anshu(n):
    if n <= 2:
        return 0
    return (n - 1)//2

t = int(input())

for i in range(t):
    n = int(input())
    print(anshu(n))
