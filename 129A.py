def count_ways_to_steal(n, cookies):
    total_sum = sum(cookies)
    odd_count = sum(1 for x in cookies if x % 2 == 1)
    even_count = n - odd_count
 
    if total_sum % 2 == 0:
        return even_count
    else:
        return odd_count
 
n = int(input())
cookies = list(map(int, input().split()))
 
print(count_ways_to_steal(n, cookies))
