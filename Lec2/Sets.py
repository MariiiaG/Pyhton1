# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества, 
# Вы можете совершать над ними любые стандартные операции, например, объединение, пересечение и разность.

# colors = {'red', 'green', 'blue'} 
# print(colors) # {'red', 'green', 'blue'} 
# colors.add('red') # sets can only contain unique values. So another 'red' won't change the set 
# print(colors) # {'red', 'green', 'blue'} 
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'} 
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'} 
# # colors.remove('red') # KeyError: 'red' 
# colors.discard('red') # ok. Will delete the item if it's there, but there won't be an error if there's no such item
# print(colors) # {'green', 'blue','gray'} 
# colors.clear() # { } # deletes all the items
# print(colors) # set()

# q = set() # creates a new empty set


# Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # creates a copy of set a as set c
# print(a, b, c) # {1, 2, 3, 5, 8} {2, 5, 8, 13, 21} {1, 2, 3, 5, 8}
# u = a.union(b) # {1, 2, 3, 5, 8, 13, 21} joins sets a and b. Without duplicate entries
# print(u)
# i = a.intersection(b) # {8, 2, 5} set i contains elements common for set a and b
# print(i)
# dl = a.difference(b) # {1, 3} set a - set b leaves us with items unique to set a 
# print(dl)
# dr = b.difference(a) # {21, 13}  only items unique to set b
# print(dr)
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
# print(q)


# Неизменяемое или замороженное множество(frozenset) — 
# множество, с которым не будут работать методы удаления и добавления.

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(a) # {1, 2, 3, 5, 8}
# print(b) # frozenset({1, 2, 3, 5, 8})