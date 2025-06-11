def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if 2 * min(a[i], a[i + 1]) > max(a[i], a[i + 1]):
            print("YES")
            return
    print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
