def tc():
    s = input()
    s = s[:-2]  # remove last two characters
    print(s + 'i')

T = int(input())
for _ in range(T):
    tc()
