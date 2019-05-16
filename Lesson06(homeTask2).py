def sort_pas(num):
    for i in range(1, (len(num))):
        while num[i] < num[i-1] and i > 0:
                num[i], num[i-1] = num[i-1], num[i]
                i -= 1
                print(num)
    return num


list_num = [2, 7, 9, 3, 1, 8, 6, 4, 0, 5]
sort_pas(list_num)