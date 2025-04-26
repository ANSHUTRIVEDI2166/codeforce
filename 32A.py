n,d= map(int,input().split())
array = list(map(int, input().split()))
count = 0

for i in range(n):
  for j in range(i+1,n):
    if abs(array[i] - array[j]) <= d:
      count+=2

print(count)
