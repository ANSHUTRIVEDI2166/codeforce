def anshu(n,k):
    x = max(1,n-k+1)
    
    def sl(m):
        return m*(m+1)*(2*m+1)//6
    
    tl = sl(n)-sl(x-1)
    
    return "YES" if tl%2 == 0 else "NO"

t = int(input())
results = []
for i in range(t):
    n, k = map(int, input().split())
    results.append(anshu(n,k))

print("\n".join(results))
