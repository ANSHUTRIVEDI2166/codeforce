b, d = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, b):
    if arr[i - 1] >= arr[i]:
        moves = ((arr[i - 1] - arr[i]) // d) + 1
        arr[i] += d * moves
        count += moves

print(count)
