def anshu(x, y):
    print(min(x, y), max(x, y))

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    anshu(x, y)
