def sudoko(index, mat):
    # base condition
    if index == 81:
        return True

    # find the row and col for the index
    row, col = divmod(index, 9)
    # check for the cell is already filled
    if mat[row][col] != 0:
        return sudoko(index + 1, mat)

    # possible value that cell can take
    for val in range(1, 10):
        if validate_val(val, row, col, mat):
            # fill the cell with that val
            mat[row][col] = val
            solved = sudoko(index + 1, mat)
            if not solved:
                print(row, col, solved)
                # undo what you have done
                mat[row][col] = 0
            else:
                return True
    return False


def validate_val(val, row, col, mat):
    return check_row(val, row, mat) and check_col(val, col, mat) and check_cube(val, row, col, mat)


def check_row(val, row, mat):
    for col in range(9):
        if mat[row][col] == val:
            return False
    return True


def check_col(val, col, mat):
    for row in range(9):
        if mat[row][col] == val:
            return False
    return True


def check_cube(val, row, col, mat):
    row_start = row - row % 3
    col_start = col - col % 3
    for rs in range(row_start, row_start + 3):
        for cs in range(col_start, col_start + 3):
            if mat[rs][cs] == val:
                return False
    return True


if __name__ == '__main__':
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    sudoko(0, board)
    print(board)
