def anshu(n,m):
  if n >= m and (n-m)%2 == 0:
    return "YES"
  else:
    return "NO"
  
t = int(input())

for i in range(t):
  n,m = map(int,input().split())
  print(anshu(n,m))
