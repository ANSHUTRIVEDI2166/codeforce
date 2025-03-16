import sys
input = sys.stdin.readline

def tc():
    s = input().strip()
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            print(1)
            return
    print(len(s))

def main():
    t = int(input().strip())
    for _ in range(t):
        tc()

if __name__ == "__main__":
    main()
