def solve_vicious_labyrinth():
    tests = int(input())
    for _ in range(tests):
        line = input().split()
        size = int(line[0])
        magic = int(line[1])
        
        result = []
        if magic % 2 == 0:
            for i in range(1, size + 1):
                if i != size - 1:
                    result.append(size - 1)
                else:
                    result.append(size)
        else:
            for i in range(1, size + 1):
                if i != size:
                    result.append(size)
                else:
                    result.append(size - 1)
        
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve_vicious_labyrinth()
