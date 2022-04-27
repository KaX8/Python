


def menu():
    answ = input("Выберите задание: \n1. Куча аргументов \n2. Сортировка \n3. Словарь \n4. Операции со словарями \n5. Сортировка с ошибкой \n6. Кортеж и элемент  \n \n")
    if answ == "1":
        Inf(1,2,3,4,"asdasd")
    elif answ == "2":
        print(Sort([4,3,2,1,10,100]))
    elif answ == "3":
        Dict()
    elif answ == "4":
        Operations()
    elif answ == "5":
        print(CheckSort([4,3,2,1,10,100]))
    elif answ == "6":
        print(DeleteFirstEl([4,3,2,1,10,100], 1))
    else:
        print("Давай еще раз спросим.")

    input("\nПродолжаем?")
    print("\n")

class CustomError(Exception):
    pass

def Inf(*args):
    a = []

    for arg in args: 
        a.append(arg)

    print("\nАругменты:")
    for i in range(len(a)): 
        print(a[i])

def Sort(rawList):
    goodList = []
    
    while rawList:
        minimum = rawList[0]
        for x in rawList:
            if x > minimum:
                minimum = x

        goodList.append(minimum)
        rawList.remove(minimum)   

    return f"\nУспешная сортировка по убыванию:\n{goodList}"

def Dict():
    d = dict.fromkeys(['one', 'two', 'three', 'four', 'five'])
    keys = []
    for key in d:
        keys.append(key)
    for i in range(len(d)):
        d[keys[i]] = input(f"Введите значение под ключем \'{keys[i]}\'\n")

    print(d)
    input("Следующий пункт?")

    buferValue = d[keys[len(keys) - 1]]
    d[keys[len(keys) - 1]] = d[keys[0]]
    d[keys[0]] = buferValue

    print(d)
    input("Следующий пункт?")

    d.pop(keys[1])
    print(d)
    input("Следующий пункт?")

    print("Добавляем связку \"Ключ: Значение\" ")
    key = input("Введите ключ\n")
    value = input("Введите значение\n")
    d.update({key:value})

    print(f"\nИтоговый словарь:\n{d}")

def Operations():
    dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2}
    dict_2 = {1: 12, 2: 7, 3: 1, 4: 2, 5: 2}

    print(f"Суммируем оддинаковые ключи: {sum_dct(dict_1, dict_2)}\n")
    print(f"Выбираем максимум из одинаковых ключей: {max_dct(dict_1, dict_2)}")

def sum_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))

def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

def CheckSort(someList):
    goodNums = True

    for i in someList:
        if type(i) is not int:
            goodNums = False

    if goodNums is False:
        return f"\nХотя бы один элемент не является целым числом, вот вам исходный кортеж:\n{someList}"
    else:
        return f"\nВ кортеже находятся ТОЛЬКО целые числа{Sort(someList)}"

def DeleteFirstEl(rawList, el):
    for x in rawList:
        if x == el:
            rawList.remove(x) 
            return f"\nЭлемент \'{el}\' был удален из кортежа:\n{rawList}"
    return f"\nЭлемент \'{el}\' отсутствует:\n{rawList}"


if __name__ == '__main__':
    import re
    import random
    import math
    from typing import Counter
    from functools import reduce
    while 1: menu()

