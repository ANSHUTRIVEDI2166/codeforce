def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    t = int(data[0])
    index = 1
    results = []
    
    for i in range(t):
        n, x = map(int, data[index].split())
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        
        total_sum = sum(a)
        
        
        if total_sum == n * x:
            results.append("YES")
        else:
            results.append("NO")
    

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
