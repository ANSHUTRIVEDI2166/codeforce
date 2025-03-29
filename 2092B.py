import sys

def solve(n, a, b):
    x = y = 0

    for i in range(n):
        if (i + 1) % 2 == 1:
            if a[i] == '1':
                x += 1
        else:
            if a[i] == '1':
                y += 1

    for i in range(n):
        if (i + 1) % 2 == 1:
            if b[i] == '1':
                y += 1
        else:
            if b[i] == '1':
                x += 1

    c1 = n // 2
    c2 = n - c1

    if x <= c1 and y <= c2:
        return "YES"
    return "NO"

def process():
    input = sys.stdin.read
    d = input().strip().split("\n")
    
    t = int(d[0])
    i = 1
    r = []
    
    for _ in range(t):
        n = int(d[i])
        a = d[i + 1]
        b = d[i + 2]
        i += 3
        r.append(solve(n, a, b))

    sys.stdout.write("\n".join(r) + "\n")

process()
