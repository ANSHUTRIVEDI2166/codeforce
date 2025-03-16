def minmov(lim, tar_val, st):
    if abs(tar_val) > lim * st:
        return -1

    lef, rig = 0, lim
    while lef < rig:
        mid = (lef + rig) // 2
        if mid * st >= abs(tar_val):
            rig = mid
        else:
            lef = mid + 1  
    
    return rig  

def main():
    tc = int(input().strip())  
    res = []

    for _ in range(tc):
        lim, tar_val, st = map(int, input().split())  
        res.append(str(minmov(lim, tar_val, st)))  

    print("\n".join(res))

main()
