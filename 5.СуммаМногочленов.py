# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


with open('file_5_1.txt', 'w') as data:
    result = '11x^6+27x^5+19x^4+71x^3+2x^2+27x^1+24x^0 = 0'
    data.writelines(f'{result}')
    
data.close()

with open('file_5_2.txt', 'w') as data:
    result = '71x^3+2x^2+27x^1+24x^0 = 0'
    data.writelines(f'{result}')
    
data.close()

file = open("file_5_1.txt")
a = file.read()
file = open("file_5_2.txt")
b = file.read()

print(a)
print(b)

c = a[:-4]+'+'+ b
print(c)

with open('file_5_3.txt', 'w') as data:
    result = c 
    data.writelines(f'{result}')
    
data.close()
