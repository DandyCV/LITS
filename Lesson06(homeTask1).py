def sort_bub(num):
    n = 0
    while n < len(num):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
                print(num)
        n += 1
    return num


list_num = [2, 7, 9, 3, 1, 8, 6, 4, 0, 5]
sort_bub(list_num)