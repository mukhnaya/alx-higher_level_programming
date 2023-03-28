#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    new_list_elements = 0
    for pau in range(list_length):
            try:
                new_list_elements = my_list_1[pau] / my_list_2[pau]
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
                new_list.append(new_list_elements)
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
