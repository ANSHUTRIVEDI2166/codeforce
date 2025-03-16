import sys
input = sys.stdin.read

def cf(x):
    if anshu(x) or anshu(x + 1):
        return -1
    
    p = 1
    while p * 2 < x:
        p *= 2
    
    return p - 1

def anshu(x):
    return (x & (x - 1)) == 0

def main():
    data = input().strip().split()
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        x = int(data[i])
        results.append(str(cf(x)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
