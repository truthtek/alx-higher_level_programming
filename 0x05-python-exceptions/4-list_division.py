#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                result = element_1 / element_2
                result_list.append(result)
            except TypeError:
                print("wrong type")
                result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except IndexError:
                print("out of range")
                result_list.append(0)
    finally:
        return result_list
