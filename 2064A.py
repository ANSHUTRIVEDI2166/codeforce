def solve():
    n = int(input())
    s = input().strip()

    ans = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            ans += 1

    if s[0] == '1':
        ans += 1
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()
