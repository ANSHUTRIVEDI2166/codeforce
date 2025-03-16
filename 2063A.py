for i in range(int(input())):
    anshu,ansiuu=map(int,input().split())
    if anshu==ansiuu==1:
        print(1)
    else:
        print(ansiuu-anshu)
