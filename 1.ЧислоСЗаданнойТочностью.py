# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# decimal функция


from decimal import Decimal
num = (input('vvedite chislo '))
D = input('vvedite tochnost ')
number = Decimal(num)
number = number.quantize(Decimal(D))
print(number)   


