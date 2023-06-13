# Алгоритмы 
# Алгоритмом называется набор инструкций для выполнения некоторой задачи. 
# В принципе, любой фрагмент программного кода можно назвать алгоритмом

# Быстрая сортировка 
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать. 
# Обозначим друзей, друг_1 это Иван, который загадал число, друг_2 это Петр, который отгадывает. 
# алгоритм бинарного поиска, который также принадлежит стратегии “разделяй и властвуй”.

# def quick_sort(array) :
#     if len(array) <= 1 : # basis for exit
#         return array 
#     else :
#         pivot = array[0] # 1st element of unordered list/ array
#     less = [i for i in array[1:] if i <= pivot] # creating 2 new arrays 
#     greater = [i for i in array[1:] if i > pivot] # to store digits smaler and greater than pivot
#     return quick_sort(less) + [pivot] + quick_sort(greater) # pivot in [], otherwise will be am error

# print(quick_sort([3, 4, 5, 12, 65, 764, 5, 38, 87])) # [3, 4, 5, 5, 12, 38, 65, 87, 764]


# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1 :
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else :
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [3, 4, 5, 676, 4, 64, 23, 356, 86, 23, 4, 76, 2, 5]
merge_sort(list1)
print(list1)