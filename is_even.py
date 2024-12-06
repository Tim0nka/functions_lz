#Создаём функцию
def chet(x):
    if x%2 == 0:
        print("Четная")
    else:
        print("Не четная")

#Передаём значение функции
r = ((input('Введите число: ')))
print(r)
r = r.split('.')
r = r[0]
print(r)
r = int(r[-1])
print(r)
#Вызываем функцию
chet(r)