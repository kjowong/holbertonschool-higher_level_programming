#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_length = len(sentence)
    if tuple_length == 0:
        tup = (0, None)
    else:
        tup = (tuple_length, sentence[0])
    return tup
