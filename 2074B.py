import sys
input = sys.stdin.read

def anshu(n, a):
    if n == 1:
        return a[0]
    return sum(a) - (n - 1)

def main():
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    results = []
    for i in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        index += 2
        results.append(str(anshu(n, a))) 
    print("\n".join(results))

if __name__ == "__main__":
    main()
