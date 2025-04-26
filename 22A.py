t = int(input())
array = list(map(int, input().split()))

s = list(set(array))
s.sort()

if len(s) > 1:
    print(s[1])
else:
    print("NO")
