##Создаём функцию
def palindrom(b: str) -> bool:
    b = b.lower()

    for i in b: #проверяем всю строку на пробелы
        if i == ' ': 
            b = b[:b.index(i)] + b[b.index(i)+1:] #вырезаем каждый пробел

    for i in range(len(b)//2):

        if b[i] != b[-(i+1)]:

            return False #если два последних числа не совпадают, то выводит False
        
    return True #если жо этого не вывело False, то выведет True


#Делаем ввод
user_input = str(input('Введите строку: '))

#Делаем вывод
if palindrom(user_input) is True:
    print('Ваша строка является палиндром')

elif palindrom(user_input) is False:
    print('Ваша строка не является палиндромом')