def max_matches(n, m, containers):
    # Sort by matches per box (bi), descending
    containers.sort(key=lambda x: -x[1])
    
    total_matches = 0
    for ai, bi in containers:
        if n == 0:
            break
        take = min(ai, n)
        total_matches += take * bi
        n -= take

    return total_matches

# Sample Input
n, m = map(int, input().split())
containers = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(max_matches(n, m, containers))
