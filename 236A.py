s = input()
c = 0
v = []

for x in s:
    if x not in v:
        v.append(x)
        c += 1

if c % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
