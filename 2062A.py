import sys

input = sys.stdin.read
data = input().split()

T = int(data[0])
results = []

for i in range(1, T + 1):
    s = data[i]
    ans = sum(int(c) for c in s)
    results.append(str(ans))

sys.stdout.write("\n".join(results) + "\n")
