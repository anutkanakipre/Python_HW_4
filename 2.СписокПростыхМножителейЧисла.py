# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите N: "))
sieve = set(range(2, n+1))
naturalnumbers =[]
while sieve:
    prime = min(sieve)
    naturalnumbers.append(prime)
    sieve -= set(range(prime, n+1, prime))
print('Простые множители:')
for i in naturalnumbers:
    if n%i==0:
        print(i)
