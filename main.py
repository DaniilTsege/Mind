
from math import pi, pow,sqrt, tan



def SCircle(r):
    # Программа поиска площади круга, где r - радиус

    print (round(pi * pow(r, 2),2 ))
    return round(pi * pow(r, 2))

def STriangle(a, b, c):
    #программа поиска площади треугольника с проверкой, является ли треугольник прямоугольным
    #где a, b, c - длины сторон треуголньика
    if a + b > c and a + c > b and b + c > a:
        #проверяем треугольник прямоугольный ли он
        if (pow(a,2) + pow(b,2) == pow(c,2)):
            print('Треугольник прямоугольный с площадью ', round((a*b)/2,2))
            return round((a*b)/2,2)
        elif (pow(a,2) + pow(c,2) == pow(b,2)):
            print('Треугольник прямоугольный с площадью ', round((a*c)/2,2))
            return round((a*c)/2,2)
        elif (pow(c,2) + pow(b,2) == pow(a,2)):
            print('Треугольник прямоугольный с площадью ', round((c*b)/2,2))
            return round((c*b)/2,2)
        else:
            # Вычисляем площадь по формуле Герона
            s = (a + b + c) / 2
            sq = sqrt(s * (s - a) * (s - b) * (s - c))
            print('Треугольник не прямоугольный с площадью', sq)
            return round(sq, 2)
    else:
        return 'Треугольника с такими сторонами не существует'

#функция нахождения площади правильного многогранника. Я, если честно, не понял пункт
# про добавление фигур и вычисление площади без знания формы
def SMnogogrannik(n, s):
    h = n * pow(s,2)
    sq = h /(4 * tan(pi / n))
    return round(sq, 2)

# Press the green button in the gutter to run the script.



