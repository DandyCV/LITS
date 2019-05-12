def num_list(st):
    st = st.split()
    n_list = []
    for x in st:
        num = "".join(n for n in x if n.isdigit())
        if num == '':
            continue
        n_list.append(int(num))
    print(n_list)


num_list('abc83 cde7 1 b 24')