#Создаём функцию
def temp(t):
    F = (t*9/5)+32
    print("По Фаренгейту:", F)


#Передаём значение функции
c = int(input('Введите значение температуры: '))
#Вызываем функцию
temp(c)