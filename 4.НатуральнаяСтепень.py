# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Комментарий от Николая:
# 
# k = 5

# x^5 + x^4 + x^3 + x^2 +x^1 + x^0 = 0
# a b c d e f
# randint(0,100)
from random import randint

k = int(input('Введите натуральную степень k: '))

list_big = []

for x in range(k,0,-1):
    koef = randint(1, 100)
    list_big.append(str(koef)+'x^'+str(x)+'+')
koef = randint(1, 100)
list_big.append(str(koef)+'x^0'+' = 0')

print(list_big)
result=''

for z in list_big:
    result = result + z
print(result)

with open('file_4.txt', 'w') as data:
    data.writelines(f'{result}\n')
    
data.close()
