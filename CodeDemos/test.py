from typing import List

def replace_missing_quizzes(quizzes: List[float]):
    """If no more than 3 quizzes are 0.0, replace them by the average
    of the remaining scores. Otherwise the list is not modified.
    """
    missing_counter = 0
    quiz_sum = sum(quizzes)
    for quiz in quizzes:
        if quiz == 0:
            missing_counter += 1
    if missing_counter > 3:
        return quizzes
    avg = quiz_sum / (len(quizzes) - missing_counter)
    for quiz_i in range(len(quizzes)):
        if quizzes[quiz_i] == 0:
            quizzes[quiz_i] = avg
    return

scores = [15.0, 0.0, 3.0, 12.0]
replace_missing_quizzes(scores)
assert scores == [15.0, 10.0, 3.0, 12.0]

scores = [15.0, 0.0, 0.0, 3.0, 12.0, 0.0, 7.0, 0.0]
replace_missing_quizzes(scores)
assert scores == [15.0, 0.0, 0.0, 3.0, 12.0, 0.0, 7.0, 0.0]

print("Complete!")

def some_col_all_pos(m: List[List[int]]) -> bool:
    """True iff some column is all greater than zero.
    m is assumed to be a rectangular matrix (all rows are the same length)
    Examples: some_col_all_pos([]) == False because it has no columns
    some_col_all_pos([[]]) == False because it has no columns
    some_col_all_pos([[42]]) == True but some_col_all_pos([[0]])) == False
    some_col_all_pos([[1, 0], [2, -3]]) == True because [1,2] is all positive
    some_col_all_pos([[0, 0, 1, 1],[1, 2, 3, 4], [8, 7, 1, 0]])
    == True because [1, 3, 1] is all positive
    """
    if len(m) == 0:
        return False
    col_num = len(m[0])
    for col_i in range(col_num):
        flag1 = True
        for row in m:
            if row[col_i] <= 0:
                flag1 = False
        if flag1:
            return True
    return False

assert not some_col_all_pos([[]])
assert some_col_all_pos([[42]])
assert not some_col_all_pos([[0]])
assert some_col_all_pos([[1, 0], [2, -3]])
assert some_col_all_pos([[0, 0, 1, 1],[1, 2, 3, 4], [8, 7, 1, 0]])
print("Complete!")

class Tree:
    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""
        raise NotImplementedError("Hey! You forgot!")

class Leaf(Tree):
    def __init__(self, v: int):
        self.value = v

    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""
        if min_val <= self.value <= max_val:
            return self.value
        return 0

class Inner(Tree):
    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""
        return self.left.sum_in_range(min_val, max_val) + self.right.sum_in_range(min_val, max_val)

t = Inner(Leaf(5), Inner( Inner(Leaf(8), Leaf(3)), Leaf(6)))
assert t.sum_in_range(4,7) == 11
assert t.sum_in_range(-3, -5) == 0
assert t.sum_in_range(0,10) == 22

print("Complete!")