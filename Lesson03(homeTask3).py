def high_year(year):
    if year % 4 == 0:
        print(year, '- високосний рік')
    else:
        print(year, '- невисокосний рік')

high_year(2019)