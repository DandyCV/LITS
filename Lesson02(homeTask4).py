command = ()
while command != 'exit':
    number_1 = input('Введіть перше число: ')
    number_2 = input('Введіть друге число: ')
    oper = input('Введіть математичну операцію над числами(+,-,*,/) ')
    if oper == '+':
        answer = float(number_1) + float(number_2)
    elif oper == '-':
        answer = float(number_1) - float(number_2)
    elif oper == '*':
        answer = float(number_1) * float(number_2)
    elif oper == '/':
        answer = float(number_1) / float(number_2)

    print ('Відповідь =', answer)
    command = input('Натисніть "Enter" щоб повторити обчислення або введіть "exit" для виходу: ')