n, k = map(int, input().split())
a = list(map(int, input().split()))
 
threshold = a[k - 1]
count = sum(1 for score in a if score >= threshold and score > 0)
 
print(count)
