# Функция enumerate

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор 
# с кортежами из индекса и элементов входных данных.
# Функция enumerate() позволяет пронумеровать набор данных.

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


my_list = list('sgdakdjhssfgdy')

# for i in range(len(my_list)):  # without using enumerate function   
#     print(f'{i+1}. {my_list[i]}')

for i in enumerate(my_list, 23): # 23 will be the first number in the ordered list
    print(i)
    
for i, item in enumerate(my_list):
    print(f'{i}. {item}')