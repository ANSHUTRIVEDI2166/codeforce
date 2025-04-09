def solve(k):
    index = 0
    count = 1
    for i in range(1, len(k)):
        if k[i] != '0':
            index = i
    for i in range(index, -1, -1):
        if k[i] == '0':
            count += 1
    print(len(k) - count)

t = int(input())
for i in range(t):
    k = input()
    solve(k)
