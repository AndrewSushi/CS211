def all_same(l: list) -> bool:
    if len(l) != 0:
        for i in l:
            if l[0] != i:
                return False
    return True

def dedup(l: list) -> list:
    new_list = []
    previous = None
    for i in l:
        if i == previous:
            previous = i
            continue
        new_list.append(i)
        previous = i
    return new_list

def max_run(l: list) -> int:
    if len(l) == 0:
        return 0
    highest_run = 0
    current_run = 0
    curr = l[0]
    for i in l:
        if i == curr:
            current_run += 1
            highest_run = max(highest_run, current_run)
        else:
            curr = i
            highest_run = max(highest_run, current_run)
            current_run = 1
    return highest_run