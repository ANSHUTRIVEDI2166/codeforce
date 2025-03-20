a,b = map(int,input().split())
count = 0
x = min(a,b)
y = max(a,b) - x

for i in range(x):
  count += 1

count2 = y // 2

print(count, count2)
