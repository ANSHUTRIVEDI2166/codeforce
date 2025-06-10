def solve():
    x = int(input())
    ans = 0
    a1 = a2 = a3 = 0
    while min(a1, a2, a3) < x:
        if a1 <= a2 and a1 <= a3:
            a1 = min(a2, a3) * 2 + 1
        elif a2 <= a1 and a2 <= a3:
            a2 = min(a1, a3) * 2 + 1
        else:
            a3 = min(a1, a2) * 2 + 1
        ans += 1
    print(ans)

def main():
    tests = int(input())
    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()
