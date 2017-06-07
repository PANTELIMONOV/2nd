# Задание 1
# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.


# coordinates:
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

# distance function:
def distance (x1,y1,x2,y2):

    return 0.5**((x1-x2)**2+(y1-y2)**2)

print(distance(x1,y1,x2,y2))

