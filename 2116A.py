def solve():
    a, b, c, d = map(int, input().split())
    if min(a, c) >= min(b, d):
        print("Gellyfish")
    else:
        print("Flower")

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
