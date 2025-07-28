def solve(n, a, b, c, d, e, intervals):
    p = 0

    for i in range(n):
        x, y = intervals[i]
        p += (y - x) * a

        if i < n - 1:
            z = intervals[i + 1][0] - y

            if z <= d:
                p += z * a
            elif z <= d + e:
                p += d * a + (z - d) * b
            else:
                p += d * a + e * b + (z - d - e) * c

    return p


n, a, b, c, d, e = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

print(solve(n, a, b, c, d, e, intervals))
