result =''
name_1 = input("Имя")
name_2 = input("Фамилия")
name = name_1 + '' + name_2
age = int(input('Возраст'))
weight = int(input('Вес'))

if age <= 30 and 135 >= weight >= 50:
    result = 'Красавчик'
elif weight > 120 or weight < 50:
    if age > 40 or age < 10:
        result = 'Боров'
    elif weight > 80:
        result = "Древний рус"
else:
    result = 'mama mia, кто ты воин ?'
print ('пацик', name, age, result)
