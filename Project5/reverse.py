from typing import List

def rev(values: List) -> List:
    return [values[element] for element in range(len(values) -1, -1, -1)]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rev(list1))