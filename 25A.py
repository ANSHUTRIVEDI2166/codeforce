t = int(input())
arr = list(map(int, input().split()))

for i in range(t - 2):
    if arr[i] % 2 == arr[i + 1] % 2:
        if arr[i + 2] % 2 != arr[i] % 2:
            print(i + 3)
            break
    elif arr[i] % 2 == arr[i + 2] % 2:
        print(i + 2)
        break
    else:
        print(i + 1)
        break
