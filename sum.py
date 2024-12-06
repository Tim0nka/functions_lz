#Cоздаем функцию
def sum(b: str) -> int:
    s = 0
    b = b.split()

    for i in b:
        i = int(i)
        s += i
    return s


#Делаем ввод
user_input = str(input('Введите список чисел: '))


#Вызываем функцию
print('Сумма всех чисел списка:', sum(user_input))