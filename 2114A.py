t = int(input())

for _ in range(t):
    num = int(input())
    flag = False
    a = b = 0

    for i in range(101):
        for j in range(101):
            if (i + j) * (i + j) == num:
                a = i
                b = j
                flag = True
                break
        if flag:
            break

    print(f"{a} {b}" if flag else -1)
