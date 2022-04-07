
def menu():
    answ = input("Выберите задание: \n1. Сумма квадратов \n2. Максимум, с условиями. \n3. Таблица умножения. \n4. Считаем символ. \n5. Сортировка чисел. \n6. Траспортировка матрицы. \n7. Расстояние. \n8. Умножение без умножения. \n9. Перевод в десятичную СС. \n \n")
    if answ == "1":
        SqrtSum()
    elif answ == "2":
        MaxFact()
    elif answ == "3":
        Multiplication()
    elif answ == "4":
        Search()
    elif answ == "5":
        Sort()
    elif answ == "6":
        Matrix()
    elif answ == "7":
        Coods()
    elif answ == "8":
        Multiply()
    elif answ == "9":
        BinToDec()
    else:
        print("Давай еще раз спросим.")

    input("\nПродолжаем?")
    print("\n")

class CustomError(Exception):
    pass

def SqrtSum():
    try:
        print("Введите K")
        k = int(input())
        print("Введите M")
        m = int(input())

        if k > m:
            a = k
            k = m
            m = a

        answ = 0
        print("Сумма квадратов от {0} до {1} равна:".format(k,m))
        while k <= m:
            answ += math.pow(k,2)
            k += 1
        print(answ)

    except:
        print("Вы что то не то ввели...")

def MaxFact():
    answ = 0
    try:
        k = int(input("Введите N:"))
        if k <= 0:
            raise CustomError("Число должно быть больше 0")
        
        for i in range(k):
            if Fact(i) <= k:
                answ = i

        print("!{0} = {1}, что не превышает {2}".format(answ, Fact(answ), k))
        return

    except ValueError:
        print("Вы должны ввести число!!!")
    except Exception as e:
        print(e)
    finally:
        MaxFact()

def Fact(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return a * Fact(a-1)

def Multiplication():
    print("Таблица умножения:")
    print("|2:|\t\t|3:|\t\t|4:|\t\t|5:|\t\t|6:|\t\t|7:|\t\t|8:|\t\t|9:|")
    string = ""
    for i in range(2, 10):
        for j in range(2, 10):
            string += "{1} * {0} = {2}\t".format(i,j,i*j)
        print(string)
        string = ""

def Search():
    while True:
        string = input("Введите строку.\n")
        if re.match("^([A-Z]|[a-z])+$", string) is not None:
            break
        else:
            print("Вы должны ввести только буквы англ. алфавита!")

    c = input("Введите любой символ.\n")

    print("Символ \'{0}\' встречается в в строке {1} раз.".format(c, string.count(c)))

def Sort():
    a = []

    while 1:
        try:
            for i in range(10):
                print("Введите {0} число:".format(i+1))
                a.append(int(input()))
            a.sort()

            print("Отсортированный набор чисел:")
            for i in a:
                print(i)
            break
        except:
            print("Вводите только числа!")

def MatrixGen():
    return [random.randint(1,9)]

def Matrix():
    a = [[random.randint(1,9)] for i in range(5)]
    b = [[0] * len(a) for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a)):
            b[i][j] = a[j][i]

    print("Оригинальная матрица:")
    for row in a:
        print(' '.join([str(elem) for elem in row]))
    print("\nМатрица, повернутая на 90 градусов:")
    for row in b:
        print(' '.join([str(elem) for elem in row]))

def Coods():
    while True:
        try:
            x = float(input("Введите X:\n"))
            y = float(input("Введите Y:\n"))

            answ = math.sqrt(math.pow((0 - x),2) + math.pow((0 - y),2))

            print("Расстояние между [0.0;0.0] и [{1};{2}] равно {0}".format(answ,x,y))
            break
        except:
            print("Координата введена неверно!")
    
def Multiply():
    while True:
        try:
            x = int(input("Введите X:\n"))
            y = int(input("Введите Y:\n"))
            answ = 0;

            print("Умножаем {0} на {1} без умножения:".format(x, y))
            for i in range(y):
                print("Шаг {0}. {1} + {2} = {3}".format(i+1, answ, x, answ+x))
                answ += x

            print("Ответ: {0} * {1} = {2}".format(x, y, answ))
            break
        except:
            print("Введите число правильно!!")

def BinToDec():
    answ = 0.0
    while True:
        try:
            a = input("Введите двоичное вещественное число:")
            if re.match("^[0-1]+[.][0-1]+$", a) is not None:
                splitted = a.split('.')
                start = len(splitted[0]) - 1

                ints = []
                for i in range(2):
                    for j in range(len(splitted[i])):
                        ints.append(int(splitted[i][j]))

                for i in ints:
                    answ += i * math.pow(2,start)
                    start -= 1

                print("Двоичное число {0} в десятичной системе счисления равно {1}".format(a,answ))
                break
            else:
                raise CustomError("\nЧисло неверное. Должно состоять только из нулей и единиц и иметь одну точку\nПример: 10.10101\n")
        except Exception as e:
            print(e)
    
    

if __name__ == '__main__':
    import re
    import random
    import math
    while 1: menu()
