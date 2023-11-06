#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if  length == 0:
        return 
    max = my_list[0]
    for number in my_list:
        if number > max:
            max = number
            return max
