import sys

input = sys.stdin.read

def solve():
    data = input().strip().split("\n")
    t = int(data[0])
    idx = 1
    res = []
    
    for _ in range(t):
        n, k = map(int, data[idx].split())
        idx += 1
        
        mp = [0] * k
        
        for _ in range(k):
            b, c = map(int, data[idx].split())
            idx += 1
            mp[b - 1] += c
        
        mp.sort(reverse=True)
        
        res.append(str(sum(mp[:n])))
    
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    solve()
