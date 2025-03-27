def max_fibonacciness(t, test_cases):
    results = []
    for a1, a2, a4, a5 in test_cases:
        max_count = 0
        
        candidates = [a1 + a2, a4 - a2, a5 - a4]
        
        for a3 in candidates:
            count = 0
            if a1 + a2 == a3:
                count += 1
            if a2 + a3 == a4:
                count += 1
            if a3 + a4 == a5:
                count += 1
            max_count = max(max_count, count)
        
        results.append(max_count)
    
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = max_fibonacciness(t, test_cases)

for res in results:
    print(res)
