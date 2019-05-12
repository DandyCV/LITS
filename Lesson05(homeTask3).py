def s_word(words):
    w_list = words.split()
    l_w = float('inf')
    for i in w_list:
        if len(i) < l_w:
            l_w = len(i)
    print('Довжина найкоротшого слова = {}'.format(l_w))


s_word('Hello my name is Jack')