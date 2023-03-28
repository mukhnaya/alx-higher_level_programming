#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    new_list_elements = 0
    try:
        for mos, jul in zip(my_list_1, my_list_2):
            new_list_elements = mos / jul
            new_list.append(new_list_elements)
    except TypeError:
        print("wrong type")
        new_list_elements = 0
    except ZeroDivisionError:
        print("division by 0")
        new_list_elements = 0
    except IndexError:
        print("out of range")
        new_list_elements = 0
    finally:
        new_list
    return new_list

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
