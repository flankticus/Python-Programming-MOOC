# Write your solution here
def column_correct(sudoku: list, column_no: int):
    check_list = []
    for row in sudoku:
        num = row[column_no]
        if num in check_list and num > 0:
                return False
        check_list.append(num)
    return True
