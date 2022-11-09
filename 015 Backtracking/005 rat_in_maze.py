def check(i, j, mat, m, n, path=None, is_path=False):
    # base condition
    # 1. rat reaches the exit
    if path is None:
        path = []
    if i == n - 1 and j == m - 1:
        print(path)
        return True, path
    # 2. Out of boundary
    if i < 0 or i >= n or j < 0 or j >= m:
        return False, path
    # 3. Visited cell or blocked cell
    if mat[i][j] == 0 or mat[i][j] == 2:
        return False, path

    # mark the cell ah visited
    mat[i][j] = 2

    # go the up direction
    if not is_path:
        path.append("U")
        is_path, path = check(i - 1, j, mat, n, m, path, is_path)
        if not is_path:
            path.pop()

    # go bottom
    if not is_path:
        path.append("D")
        is_path, path = check(i + 1, j, mat, n, m, path, is_path)
        if not is_path:
            path.pop()

    # go to left
    if not is_path:
        path.append("L")
        is_path, path = check(i, j - 1, mat, n, m, path, is_path)
        if not is_path:
            path.pop()

    # go to right
    if not is_path:
        path.append("R")
        is_path, path = check(i, j + 1, mat, n, m, path, is_path)
        if not is_path:
            path.pop()

    return is_path, path


if __name__ == '__main__':
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    print(check(0, 0, maze, 4, 4))
