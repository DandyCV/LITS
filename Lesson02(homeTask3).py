number = input('Введіть ціле число: ')
number_odd = 0
number_even = 0
for i in number:
    if int(i) % 2 == 0:
        number_even +=1
    if int(i) % 2 == 1:
        number_odd +=1
print ('Кількість непарних цифр =', number_odd)
print ('Кількість парних цифр =', number_even)