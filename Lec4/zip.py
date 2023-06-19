#  Функция zip

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор 
# с кортежами из элементов входных данных

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# # Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333] # only 3 entries
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)] # left with only 3 entries here


# let_list = list('hfsdkjfhkdsfhk')
# num_list = list('1263764938')

# new_list = list(zip(let_list, num_list))

# print(new_list) # will only zip till the end of the shortest list


from itertools import zip_longest

let_list = list('hfsdkjfhkdsfhk')
num_list = list('12637649')
punct_list = list('#&^@#(#*@^^#)')

new_list = list(zip_longest(let_list, num_list, punct_list, fillvalue='Ooops')) # can skip the fillvalue

print(new_list) # will go till the last element and replace the missing ones with 'none' if no fillvalue set