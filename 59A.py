t = input()

s = 0
c = 0

for char in t:
    if char.islower():
        s += 1
    elif char.isupper():
        c += 1

if s >= c:
    t = t.lower()
else:
    t = t.upper()

print(t)
