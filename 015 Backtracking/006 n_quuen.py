def n_queen(row, n: int, placed_col=None, placed_ld=None, placed_rd=None, mat=None):
    # Initialising
    if mat is None:
        mat = [[0]*n for _ in range(n)]
    if placed_rd is None:
        placed_rd = [0] * 2 * n
    if placed_ld is None:
        placed_ld = [0] * 2 * n
    if placed_col is None:
        placed_col = [0] * n
    # base condition
    # When we placed all queen successfully
    if row == n:
        print(mat)
        return
    for col in range(n):
        # check for any queen have the path to current cell
        if placed_col[col] == 1 or placed_ld[n + row - col] == 1 or placed_rd[row + col] == 1:
            continue

        mat[row][col] = 1
        placed_col[col] = 1
        placed_ld[n + row - col] = 1
        placed_rd[row + col] = 1
        n_queen(row + 1, n, placed_col, placed_ld, placed_rd, mat)
        # undo what you have done
        mat[row][col] = 0
        placed_col[col] = 0
        placed_ld[n + row - col] = 0
        placed_rd[row + col] = 0


if __name__ == '__main__':
    n_queen(0, 4)
