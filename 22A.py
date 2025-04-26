t = int(input())
array = []

for i in range(t):
    array.append(int(input()))

s = list(set(array))
s.sort()

if len(s) > 1:
    print(s[1])
else:
    print("NO")
