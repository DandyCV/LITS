number = input('Введіть ціле число: ')
number_summ = 0
number_prod = 1
for i in number:
    number_summ = ( number_summ + int(i))
    if int(i) > 0:
        number_prod = (number_prod * int(i))
print ('Сума цифр =', number_summ)
print ('Добуток цифр =', number_prod)