def is_symmetric(matrix):
    symmetric_pairs = [
        ((0, 0), (2, 2)),
        ((0, 1), (2, 1)),
        ((0, 2), (2, 0)),
        ((1, 0), (1, 2))
    ]
    
    for (i1, j1), (i2, j2) in symmetric_pairs:
        if matrix[i1][j1] != matrix[i2][j2]:
            return "NO"
    
    return "YES"

matrix = [input().strip() for _ in range(3)]
print(is_symmetric(matrix))
