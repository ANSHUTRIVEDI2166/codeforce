import sys
input = sys.stdin.read

def solve():
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        digits = list(map(int, data[index + 1].split()))
        index += 2
        
        cnt = [0] * 10
        found = False
        
        for i in range(n):
            cnt[digits[i]] += 1
            if cnt[0] >= 3 and cnt[1] >= 1 and cnt[2] >= 2 and cnt[3] >= 1 and cnt[5] >= 1 and not found:
                results.append(str(i + 1))
                found = True
        
        if not found:
            results.append('0')
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
