s = list(map(int, input().split()))
s.sort()


for i in range(2, 4):
    if s[i - 2] + s[i - 1] > s[i]:
        print("TRIANGLE")
        exit()


for i in range(2, 4):
    if s[i - 2] + s[i - 1] == s[i]:
        print("SEGMENT")
        exit()

print("IMPOSSIBLE")
