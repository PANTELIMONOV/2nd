# Задание 3
# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.

a=int(input())
b=int(input())
c=int(input())

def triangle (a,b,c):
    if a+b>c and b+c>a and a+c>b:
        print('True')
    else:
        print('False')

triangle (a,b,c)