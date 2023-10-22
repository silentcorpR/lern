while True:
    x = float(input('введите число'))
    if 0.0 <= x <= 10.0:
        print ('Результат: ', x**2)
        break
    else:
        print (x,'Неверно, введите число от 0 до 10')
