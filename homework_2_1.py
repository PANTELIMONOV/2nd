# Задание 1
# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

def distance (x1,y1,x2,y2):
    if x1>=y1 :
        print(x1-y1)
    else:
        print(y1-x1)
    if x2>=y2 :
        print(x2-y2)
    else:
        print(y2-x2)

distance(x1,y1,x2,y2)

