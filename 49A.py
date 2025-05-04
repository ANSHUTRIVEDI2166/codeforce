t = input().strip()

v = {'a', 'e', 'i', 'o', 'u', 'y'}

for ch in reversed(t):
    if ch.isalpha():
        if ch.lower() in v:
            print("YES")
        else:
            print("NO")
        break
