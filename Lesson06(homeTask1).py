def sort_bub(list_num):
    for i in range(len(list_num)-1):
        for i in range(len(list_num)-1):
            if list_num[i] > list_num[i+1]:
                list_num[i], list_num[i+1] = list_num[i+1], list_num[i]
            print (list_num)
    return list_num


list_num = [2, 7, 9, 3, 1, 8, 6, 4, 0, 5]
sort_bub(list_num)