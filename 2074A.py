import math

def anshu(l, r, d, u):
   
    side1 = r + l
    side2 = u + d
 
    diag1 = math.sqrt(l ** 2 + d ** 2)
    diag2 = math.sqrt(l ** 2 + u ** 2)
    diag3 = math.sqrt(r ** 2 + d ** 2)
    diag4 = math.sqrt(r ** 2 + u ** 2)
    
    return side1 == side2 and diag1 == diag4 and diag2 == diag3 and diag1 == diag2

def main():
    t = int(input())
    for _ in range(t):
        l, r, d, u = map(int, input().split())
        if anshu(l, r, d, u):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
