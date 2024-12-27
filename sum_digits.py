#Создаём функцию
def sum(b: str) -> int:
    s = 0

    for i in b:
        i = int(i)
        s += i
    return s


#Делаем ввод
user_input = str(input('Введите число: '))


#Делаем вывод
print('Сумма всех цифр вашего числа:', sum(user_input))