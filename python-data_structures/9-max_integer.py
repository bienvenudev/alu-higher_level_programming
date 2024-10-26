#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        larg = my_list[0]

        for val in my_list:
            if val > larg:
                larg = val

    return larg
