# Задача 1
'''
    Напишите программу, которая принимае на вход цифру, обозначающую день недели,
    и проверяет, является ли этот день недели выходным
'''

print("Задача 1")
d = int(input("Введите день недели "))
if (not(1 <= d <= 7)):
    print("С какой вы планеты? На Земле нет такого дня недели!")
elif d > 5:
    print("Выходной! Отрывайтесь! :))")
else:
    print("Не выходной :(")
print()


# Задача 2
'''
    Напишите программу для проверки истиности утверждения !(X v Y v Z) = !X * !Y * !Z
    для всех значений предикат
'''

print("Задача 2")
print("Проверка закона Де Моргана таблицей истинности")
print(f'\t X \t Y \t Z \t !(X v Y v Z) \t !X * !Y * !Z \t Тождество закона')
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            left = not (X or Y or Z)
            right = not(X) and not(Y) and not(Z)
            print(f'\t {X} \t {Y} \t {Z} \t {left} \t\t\t {right} \t\t\t {left==right}')
print()


# Задача 3
'''
    Напишите программу, которая принимает на вход координаты точки (X и Y),
    причём X != 0 и Y != 0, и выдаёт номер четверти плоскости,
    в которой находится точка (или на какаой оси она находится) 
'''

print("Задача 3")
X = int(input("Введите координату х: "))
Y = int(input("Введите координату y: "))
if X == 0 and Y == 0:
    print("Обе координаты не должны одновременно равнятья нулю!")
elif X == 0:
    print("Точка лежит на оси ординат Y")
elif Y == 0:
    print("Точка лежит на оси абсцисс X")
elif X > 0 and Y > 0:
    print("Точка принадлежит 1 четверти")
elif X < 0 and Y > 0:
    print("Точка принадлежит 2 четверти")
elif X < 0 and Y < 0:
    print("Точка принадлежит 3 четверти")
else:
    print("Точка принадлежит 4 четверти")
print()


# Задача 4
'''
    Напишите программу, которая по заданному номеру четверти показывает диапазон
    возможных координат точек в этой четверти 
'''

print("Задача 4")
number = int(input("Введите номер координатной четверти: "))
if not(1 <= number <= 4):
    print("В декартовой плоскости всего четыре четверти с номерами от 1 до 4!")
elif number == 1:
    print("x > 0 и y > 0")
elif number == 2:
    print("x < 0 и y > 0")
elif number == 3:
    print("x < 0 и y < 0")
else:
    print("x > 0 и y < 0")
print()


# Задача 5
'''
    Напишите программу, которая принимает на вход координаты двух точек
    и находит расстояние между ними в 2D или в 3D
'''

print("Задача 5")
# я тут позволю себе сразу определять мерность пространства по количеству введённых координат
A_input = input("Введите координаты точки A через пробел: ").split()
B_input = input("Введите координаты точки B через пробел: ").split()
if len(A_input) != len(B_input):
    print("Точки должны быть обе одновременно на плоскости или в пространстве!")
elif not(2 <= len(A_input) <= 3):
    print("Работаем только на плоскости 2D или в пространстве 3D!")
else:
    Ax = int(A_input[0])
    Ay = int(A_input[1])
    Bx = int(B_input[0])
    By = int(B_input[1])
    if len(A_input) == 2:
        dist = ((Ax - Bx)**2 + (Ay - By)**2)**0.5
        print("Расстояние между точками на плоскости равно", dist)
    else:
        Az = int(A_input[2])
        Bz = int(B_input[2])
        dist = ((Ax - Bx) ** 2 + (Ay - By) ** 2 + (Az - Bz)**2) ** 0.5
        print("Расстояние между точками в пространстве равно", dist)
print("\nСпасибо за внимание!")

