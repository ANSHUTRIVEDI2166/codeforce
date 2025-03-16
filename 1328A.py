def fun(a,b):
    if a%b==0:
        return 0
    else:
      modulus = a%b
      ans = b-modulus
      return ans

t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(fun(a,b))
