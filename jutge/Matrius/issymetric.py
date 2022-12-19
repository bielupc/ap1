def is_symmetric(m: list[list[int]]) -> bool:

    n = len(m)
    for i in range(n):
        for j in range(i + 1):
            if m[i][j] != m[j][i]:
                return False
    return True
