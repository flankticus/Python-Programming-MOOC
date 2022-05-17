# Write your solution here
def row_correct(sudoku_board: list, row_no: int):
    check_list = []
    for box in sudoku_board[row_no]:
        if box != 0:
            if box in check_list:
                return False
            check_list.append(box)
    return True