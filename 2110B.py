def solve():
    s = input()
    n = len(s)
    bal = 0
    for i in range(1, n - 1):
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            print("YES")
            return
    if bal == 0:
        print("NO")
    else:
        print("YES")

tt = int(input())
for _ in range(tt):
    solve()
