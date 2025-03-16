def check_array_existence():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    test_cases = int(data[index])
    index += 1
    results = []

    for _ in range(test_cases):
        length = int(data[index])
        index += 1
        characteristic = list(map(int, data[index:index + length - 2]))
        index += (length - 2)

        if length == 3:
            results.append("YES")
            continue

        is_possible = True
        for i in range(length - 4):
            if characteristic[i] == 1 and characteristic[i + 1] == 0 and characteristic[i + 2] == 1:
                is_possible = False
                break

        results.append("YES" if is_possible else "NO")

    sys.stdout.write("\n".join(results) + "\n")


check_array_existence()
