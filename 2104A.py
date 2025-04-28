t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    t = a + b + c
    if t % 3 != 0:
        print("NO")
    else:
        x = t // 3
        if x >= a and x >= b and x <= c:
            print("YES")
        else:
            print("NO")
