from collections import Counter

import sys
input = sys.stdin.read

def solve():
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        a = data[index + 1]
        index += 2
        
        cnt = Counter(a)
        needed = 0
        
        for _ in range(m):
            for diff in 'ABCDEFG':
                if cnt[diff] > 0:
                    cnt[diff] -= 1
                else:
                    needed += 1
        
        results.append(str(needed))
    
    print("\n".join(results))

solve()
