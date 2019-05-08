def triangle_area(a, b, c):
    p = (1/2) * (a + b + c) #p - половина перисетру
    if p > a and p > b and p > c:
        s = p * (p - a) * (p - b) * (p - c)**(0.5)
        print ('Площа трикутника зі сторонами', a , b , c, '=', s)
        return True
    else:
        print ('Трикутника зі сторонами', a , b , c, 'не існує')
        return False

print(triangle_area(11, 7 , 5))