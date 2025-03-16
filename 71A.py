n = int(input())
for i in range(n):
    anshu= input().strip()
    if len(anshu) > 10:
        print(f"{anshu[0]}{len(anshu) - 2}{anshu[-1]}")
    else:
        print(anshu)
