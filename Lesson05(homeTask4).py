def new_string(st):
    n_upp = 0
    n_low = 0
    n_lett = 0
    for i in st:
        if i.isupper():
            n_upp += 1
            n_lett +=1
        elif i.islower():
            n_low += 1
            n_lett += 1
    p_upp = 100 * n_upp / n_lett
    p_low = 100 * n_low / n_lett
    p_upp = (p_upp)

    print('Рядок складаэться з {0}% букв у верхньому регістрі і {1}% букв у нижньому регістрі'.format(p_upp, p_low))

new_string('Hello, Tom, my name is Jack!')