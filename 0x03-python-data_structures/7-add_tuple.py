#/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupa_list = list(tuple_a)
    tupb_list = list(tuple_b)
    for i in range(0, 2):
        tupa_list.append(0)
        tupb_list.append(0)
    sum1 = tupa_list[0] + tupb_list[0]
    sum2 = tupa_list[1] + tupb_list[1]
    final_tuple = (sum1, sum2)
    return final_tuple
