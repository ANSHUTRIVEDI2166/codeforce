def fb(n):
    fb = n // 15
    c = fb * 3
    rem = n % 15

    for i in range(rem + 1):
        if i % 3 == i % 5:
            c += 1

    print(c)

tc = int(input())
for x in range(tc):
    n = int(input())
    fb(n)
