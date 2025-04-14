def count_valid_x(n, a, b, h):
    h.sort()
    if h[n-a-1] < h[n-a]:
        return h[n-a] - h[n-a-1]
    else:
        return 0

n, a, b = map(int, input().split())
h = list(map(int, input().split()))
print(count_valid_x(n, a, b, h))
