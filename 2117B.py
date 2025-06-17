for _ in range(int(input())):
    n = int(input())
    if n > 1:
        print(*range(2, n + 1), 1)
    else:
        print(1)
