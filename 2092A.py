import sys

def cmg(n, beauty_levels):
    beauty_levels.sort()
    total_diff = sum(beauty_levels[i] - beauty_levels[i - 1] for i in range(1, n))
    return total_diff

def solve():
    input_data = sys.stdin.read().strip().split("\n")
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        beauty_levels = list(map(int, input_data[idx + 1].split()))
        idx += 2
        results.append(str(cmg(n, beauty_levels)))
    
    print("\n".join(results))

solve()
