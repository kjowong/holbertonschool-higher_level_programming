#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if i == idx + 1:
            my_list.remove(i)
    return my_list
