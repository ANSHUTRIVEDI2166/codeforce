import sys
input = sys.stdin.read

def solve():
    data = input().strip().split('\n')
    test_cases = int(data[0])
    res = []
    idx = 1
    
    for cases in range(test_cases):
        x, y = map(int, data[idx].split())
        idx += 1
        
        if x % 2 == 0:
            res.append(str((x + y - 2) // (y - 1)))
        else:
            res.append(str(1 + ((x - y) + y - 2) // (y - 1)))
    
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    solve()
