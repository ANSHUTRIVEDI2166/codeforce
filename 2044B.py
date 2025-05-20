t = int(input())
for _ in range(t):
    s = input()[::-1]
    s = ''.join('p' if c == 'q' else 'q' if c == 'p' else c for c in s)
    print(s)
