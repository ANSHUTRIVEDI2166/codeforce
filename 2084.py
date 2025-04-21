T = int(input())
for _ in range(T):
    n = int(input())
    if n % 2 == 1:
        print(n, end=' ')
        for i in range(1, n):
            end_char = '\n' if i == n - 1 else ' '
            print(i, end=end_char)
    else:
        print(-1)
