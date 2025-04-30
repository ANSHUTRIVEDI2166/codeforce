def solve(n):
  count = 1
  if n == 1:
    return 1
  else:
    while n >3:
      n = n//4
      count *= 2
    return count


t = int(input())

for i in range(t):
  n = int(input())
  print(solve(n))
