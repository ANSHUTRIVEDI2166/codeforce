from math import ceil

n, m, a = map(int, input().split())

answer = ceil(n / a) * ceil(m / a)

print(answer)
