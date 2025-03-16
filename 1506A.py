t = int(input())

for i in range(t):
    n,m,x = map(int,input().split())
    
    colforcm = ((x-1)//n)+1
    rowforcm = ((x-1)%n)+1

    res = (rowforcm - 1)*m + colforcm
    print(res)
