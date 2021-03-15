
import random

def read_int_from_user(msg, error_msg):
    while True:
        x = input(msg)
        try:
            x = int(x)
            break
        except:
            print(error_msg)
    return x

def read_float_from_user(msg, error_msg):
    while True:
        x = input(msg)
        try:
            x = float(x)
            break
        except:
            print(error_msg)
    return x

def read_str_from_user(msg, error_msg):
    x = input(msg)
    return x

def take_basic_values(userInput):

    if userInput == True:
        str = "number of objects (int): "
        error_str = "please enter an <int> number\n"
        number_of_objects_def = read_int_from_user(str, error_str)

        str = "max weight (float) : "
        error_str = "please enter a number\n"
        max_weight_def = read_float_from_user(str, error_str)


        str = "min value (float) : "
        error_str = "please enter a number\n"
        min_weight_def = read_float_from_user(str, error_str)

        str = "max value (float) : "
        error_str = "please enter a number\n"
        max_value_def = read_float_from_user(str, error_str)


        str = "min weight (float) : "
        error_str = "please enter a number\n"
        min_value_def = read_float_from_user(str, error_str)

        str = "sack capacity (float) : "
        error_str = "please enter a number\n"
        capacity_def = read_float_from_user(str, error_str)


        str = "file name (string) : "
        error_str = "please enter a string \n"
        file_name_def = read_str_from_user(str, error_str)

        str = "floor number at (0 for int numbers)"
        error_str = "please enter an int \n"
        floor_by_def =  read_int_from_user(str, error_str)
    else:
        number_of_objects_def = 20
        max_weight_def = 80
        min_weight_def = 10
        max_value_def = 10
        min_value_def = 1
        capacity_def = 190
        # file_name_def = "../problem_parser_w7/test"
        file_name_def = "test"
        floor_by_def = 2
    return number_of_objects_def, max_weight_def, min_weight_def,\
           max_value_def, min_value_def, capacity_def,\
           file_name_def, floor_by_def



number_of_objects, max_weight, min_weight, \
max_value, min_value, \
capacity, file_name, floor_by = take_basic_values(False)






f = open(file_name, "w")


line = str(number_of_objects) + " " + str(capacity) + "\n"
f.write(line)

for i in range(number_of_objects):

    wi = round(random.uniform(min_weight, max_weight), floor_by)
    vi = round( random.uniform(min_value, max_value), floor_by)
    line = str(vi) + " " + str(wi) + "\n"
    f.write(line)

f.close()


