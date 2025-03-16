def max_kevin_points(t, test_cases):
    results = []
    
    for n, arr in test_cases:
        evens = []
        odds = []
        
        for num in arr:
            if num % 2 == 0:
                power = 0
                while num % 2 == 0:
                    num //= 2
                    power += 1
                evens.append((power, num))
            else:
                odds.append(num)
        
        evens.sort(reverse=True, key=lambda x: x[0])
        
        sorted_arr = [e[1] * (2 ** e[0]) for e in evens] + odds

        s = 0
        points = 0
        
        for num in sorted_arr:
            s += num
            if s % 2 == 0:
                points += 1
                while s % 2 == 0:
                    s //= 2
        
        results.append(points)
    
    return results

t = int(input())
test_cases = []

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

for res in max_kevin_points(t, test_cases):
    print(res)
