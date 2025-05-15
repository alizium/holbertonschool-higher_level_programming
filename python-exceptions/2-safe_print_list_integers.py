#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    variable_counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            variable_counter += 1
        except:
            pass
    print()
    return variable_counter
