# модульность

# def max1(a, b):
#     if a > b :
#         return a # return ends the execution of the function, so no point to use 'else' after the 'if' clause
#     return b


# calling a function from another file :

# import functions 
# print(functions.sum_str('trying ', 'to ', 'call ', 'a ', 'function')) # trying to call a function

# from functions import sum_str # calling a specific function 
# print(sum_str('this ', 'is ', 'pretty ', 'neat')) # this is pretty neat

# from functions import * # will import all the functions from the file selected
# print(sum_str('Wow ', 'wooww ', '! !')) # Wow wooww ! !

import functions as f # creating an alias
print(f.sum_str('So ', 'as ', 'not to ', 'print the ', 'same word ', 'each time')) # So as not to print the same word each time