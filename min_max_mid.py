from math import fabs


#Делаем ввод
user_input = str(input('Введите список чисел: '))
user_input = user_input.split()


#Создаём функции
def f_max(b: list) -> int:
    return max(b)

def f_min(b: list) -> int:
    return min(b)

def f_mid(b: list) -> int:
    sred = 0
    for i in b:
        i = int(i)
        sred += i
    sred = sred / len(b)
    a = abs(int(b[0]) - sred) 
    chislo = b[0]

    for i in b:
        i = int(i)
        if abs(i - sred) < a:
            a = abs(i - sred)
            chislo = i
    #Вызываем функцию
    return chislo

print('Максимальное число:', f_max(user_input))
print('Минимальное число:', f_min(user_input))
print('Среднее число:', f_mid(user_input))