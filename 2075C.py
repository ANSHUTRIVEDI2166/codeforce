import sys
input = sys.stdin.read

def count():
    data = input().strip().split('\n')
    t = int(data[0])
    idx = 1
    res = []
    
    for _ in range(t):
        n, m = map(int, data[idx].split())
        idx += 1
        arr = list(map(int, data[idx].split()))
        idx += 1
        
        count = [0] * (n + 1)
        for num in arr:
            count[num] += 1
        
        prefix_sum = [0] * (n + 2)
        for i in range(n, 0, -1):
            prefix_sum[i] = count[i] + prefix_sum[i + 1]
        
        pairs = 0
        for i in range(1, n):
            left_part = prefix_sum[i]
            right_part = prefix_sum[n - i]
            intersect = prefix_sum[max(i, n - i)]
            pairs += left_part * right_part - intersect
        
        res.append(str(pairs))
    
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    count()
