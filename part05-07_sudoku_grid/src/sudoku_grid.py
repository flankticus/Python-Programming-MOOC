# Write your solution here
from re import L

from numpy import block


def row_correct(sudoku_board: list, row_no: int):
    check_list = []
    for box in sudoku_board[row_no]:
        if box != 0:
            if box in check_list:
                return False
            check_list.append(box)
    return True

def column_correct(sudoku: list, column_no: int):
    check_list = []
    for row in sudoku:
        num = row[column_no]
        if num in check_list and num > 0:
                return False
        check_list.append(num)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    check_list = []
    for row in sudoku[row_no : row_no+3]:
        for col in row[column_no: column_no+3]:
            if col > 0 and col in check_list:
                return False
            check_list.append(col)
    return True


def sudoku_grid_correct(sudoku_board: list):
    for row in range(0,9):
        if not row_correct(sudoku_board, row):
            return False

    for column in range(0, 9):
        if not column_correct(sudoku_board, column):
            return False

    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if not block_correct(sudoku_board, row, column):
                return False
    
    return True

if __name__ == "__main__":
    sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))