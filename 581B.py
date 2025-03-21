t = int(input())
floor = list(map(int, input().split()))

result = [0] * t
max_right = 0

for i in range(t - 1, -1, -1):
    if floor[i] > max_right:
        result[i] = 0
    else:
        result[i] = max_right - floor[i] + 1
    max_right = max(max_right, floor[i])

print(*result)
