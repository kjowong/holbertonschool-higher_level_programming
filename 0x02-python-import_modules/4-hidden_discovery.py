#!/usr/bin/python3
import hidden_4
lt = dir(hidden_4)
if __name__ == "__main__":
    for i in range(0, len(lt)):
        if lt[i][0] != "_" and lt[i][1] != "_":
            print(lt[i])
