
def menu():
    answ = input("Выберите задание: \n1. Куча аргументов    \n \n")
    if answ == "1":
        Inf(1,2,3,4,"asdasd")
    if answ == "2":
        Inf(1,2,3,4,"asdasd")
    else:
        print("Давай еще раз спросим.")

    input("\nПродолжаем?")
    print("\n")

class CustomError(Exception):
    pass

def Inf(*args):
    answ = "Аргументы: "
    for arg in args: answ += f"\"{arg}\" "
    print(answ)

if __name__ == '__main__':
    import re
    import random
    import math
    while 1: menu()

