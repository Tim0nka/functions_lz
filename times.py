#Создаём функцию
def time(b: str):
    b = b.split('-')
    s = int(b[0])*3600 + int(b[1])*60 + int(b[2])
    print("Секунды:", s)

#Передаём значение функции
c = input('Введите время в формате часы-минуты-секунды: ')

#Вызываем функцию
time(c)