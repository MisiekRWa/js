


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
sort_list = sorted(list_to_sort, key=lambda x: (x[1], x[2]))
print(list_to_sort)
print(sort_list)
 #fff