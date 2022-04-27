


def menu():
    answ = input("Выберите задание: \n1. Максимум \n2. Положительные числа. \n3. Тип данных. \n4. Натуральное число. \n5. Треугольник. \n6. Счастливый билет. \n7. Кирпич. \n8. Шахматные фигуры. \n \n")
    if answ == "1":
        Max()
    elif answ == "2":
        Positive()
    elif answ == "3":
        SymType()
    elif answ == "4":
        Natural()
    elif answ == "5":
        Triangle()
    elif answ == "6":
        Lucky()
    elif answ == "7":
        Brick()
    elif answ == "8":
        Chess()
    else:
        print("Давай еще раз спросим.")

    input("Продолжаем?")
    print("\n")

def Max():
    a = []

    try:
        for i in range(3):
            a.append(int(input("Вводите числа!!!\n")))
        print("Максимум:",max(a))
    except:
        print("Вы что то не то ввели, досвидания...")

def Positive():
    answ = 0
    try:
        for i in range(5):
            if int(input("Вводите числа!!!\n")) > 0: 
                answ += 1
        print("Положительных чисел:",answ)
    except:
        print("Вы что то не то ввели, досвидания...")

def SymType():
    while 1:
        smth = input("Введите один символ!")
        if len(smth) == 1:
            if re.match('[0-9]', smth) is not None:
                print(smth, "- Это число!")
            elif re.match('[A-Z]|[a-z]|[А-Я]|[а-я]', smth) is not None:
                print(smth, "- Это буква!")
            elif re.match('[-.?!)(,:]', smth) is not None:
                print(smth, "- Это знак препинания!")
            else:
                print(smth, "- Это что то еще!")
            break
        else:
            print("Нужен только один символ!")
    
def Natural():
    try:
        a = int(input("Введите число"))
        if a >= 0:
            print("Число натуральное!")
        else:
            print("Число не натуральное!")
    except Exception:
        print("Это ТОЧНО не натуральное число!")

def Triangle():
    a = []
    try:
        print("Вводите стороны треугольника:")
        for i in range(3):
            a.append(int(input()))
        if a[0] + a[1] < a[2] or a[1] + a[2] < a[0] or a[2] + a[0] < a[1]:
            print("Такого треугольника быть не может!!")
        else:
            print("Да!!! Хороший треугольник!")
    except:
        print("Вы что то не то ввели, досвидания!")

def Lucky():

    while 1:
        ticket = input("Вводите свой билетик(6 цифр):")
        nums = []
        a = 0
        b = 0

        if re.match("\D", ticket) is None:
            for i in range(6):
                nums.append(int(ticket[i]))
            for i in range(6):
                if i < 3:
                    a += nums[i]
                elif i >= 3:
                    b += nums[i]
            if a == b:
                print("Поздравляю!!! У вас счастливый билетик!")
            else:
                print("Печаль беда. Вам не повезло...")
            break
        else:
            print("Как то вы неправильно ввели... \n")

def Brick():
    brick = []
    square = []
    while 1:
        try:
            print("Вводите ребра кирпича(a,b,c) и стороны отверстия(x,y):")

            print("Кирпич(a,b,c):")
            for i in range(3):
                brick.append(float(input()))

            print("Отверстие(x,y):")
            for i in range(2):
                square.append(float(input()))

            sBr_1 = brick[0] * brick[1]
            sBr_2 = brick[1] * brick[2]
            sBr_3 = brick[2] * brick[0]

            sSq = square[0] * square[1]

            if sSq > sBr_1 or sSq > sBr_2 or sSq > sBr_3:
                print("Кирпич сможет пройти!")
            else:
                print("Не судьба, кирпич больше...")

            break
        except:
            print("Вы что то не то ввели, давайте еще раз!\n")

def Arr(num):
    flag = True
    a = []
    for i in range(num):
        a.append(input())
    for i in range(num):
        a[i] = int(a[i])
        if a[i] < 1 or a[i] > 9:
            flag = False
    return a, flag

def Chess():
    while 1:
        try:
            print("Введите 2 целых числа:\nСтартовое расположение фигуры: вертикаль, горизонталь")
            start = Arr(2)
            print("Введите 2 целых числа:\nКуда будет шагать фигура?: вертикаль, горизонталь")
            move = Arr(2)

            if not start[1] or not move[1]:
                print("Вы должны ввести числа от 1 до 8!")
            else:
                while 1:
                    pieces = ["","Ладья","Слон","Конь","Пешка"]
                    piece = int(input("Выберете фигуру:\n1.Ладья\n2.Слон\n3.Конь\n4.Пешка\n"))
                    if piece >= 1 and piece <= 4:
                        canMove = 0 #0 - не может, 1 - может, -1 = координаты одинаковые
                        print("Сможет ли фигура \"{0}\", стоящая на координатах [{1};{2}] дойти до координат [{3};{4}]?"
                              .format(pieces[piece], start[0][0], start[0][1], move[0][0], move[0][1]))

                        if start[0] == move[0]:
                            canMove = -1 
                        elif piece == 1 and (start[0][0] == move[0][0] or start[0][1] == move[0][1]):#ЛАДЬЯ
                            canMove = 1 
                        elif piece == 2: #СЛОН
                            if abs(start[0][0] - move[0][0]) == abs(start[0][1] - move[0][1]):
                                canMove = 1
                        elif piece == 3: #КОНЬ
                            if abs(start[0][0] - move[0][0]) == 1 and abs(start[0][1] - move[0][1]) == 2 or abs(start[0][0] - move[0][0]) == 2 and abs(start[0][1] - move[0][1]) == 1:
                                canMove = 1
                        elif piece == 4: #ПЕШКА
                            pawnMove = 1
                            if start[0][1] == 2:
                                pawnMove = 2
                            if start[0][1] + pawnMove == move[0][1] and start[0][0] == move[0][0]:
                                canMove = 1 
                            

                        if canMove == 0:
                            print("Фигура НЕ сможет сходить")
                        elif canMove == 1:
                            print("Фигура СМОЖЕТ сходить")
                        elif canMove == -1:
                            print("А зачем ходить? Координаты одинаковые.")
                        return
                    else:
                        print("Давайте нормальную фигуру...")
        except ValueError:
            print("Вы должны вводить целые числа!\n")


if __name__ == '__main__':
    import re
    while 1: menu()
