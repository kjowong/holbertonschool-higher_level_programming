#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for element in set_1:
        if element in set_2:
            set_1.copy()
        else:
            diff.append(element)
    for element in set_2:
        if element in set_1:
            set_2.copy()
        else:
            diff.append(element)
    return diff
