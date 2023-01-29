from typing import List

Waldo = 'W'
Other = '.'

def all_row_exists_waldo(matrix: List[List]) -> bool:
    for row in matrix:
        if Waldo not in row:
            return False
    return True

def all_col_exists_waldo(matrix: List[List]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return True
    for col_i in range(len(matrix)):
        temp_list = [row[col_i] for row in matrix]
        if Waldo not in temp_list:
            return False            
    return True

def all_row_all_waldo(matrix: List[List]) -> bool:
    for row in matrix:
        if Other in row:
            return False
    return True

def all_col_all_waldo(matrix: List[List]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return True
    for col_i in range(len(matrix)):
        temp_list = [row[col_i] for row in matrix]
        if Other in temp_list:
            return False            
    return True

def exists_row_exists_waldo(matrix: List[List]) -> bool:
    for row in matrix:
        if Waldo in row:
            return True
        continue
    return False

def exists_col_exists_waldo(matrix: List[List]) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    for col_i in range(len(matrix)):
        temp_list = [row[col_i] for row in matrix]
        if Waldo in temp_list:
            return True
        continue
    return False

def exists_row_all_waldo(matrix: List[List]):
    for row in matrix:
        if Other in row:
            continue
        return True
    return False

def exists_col_all_waldo(matrix: List[List]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    for col_i in range(len(matrix)):
        temp_list = [row[col_i] for row in matrix]
        if Other in temp_list:
            continue
        return True
    return False