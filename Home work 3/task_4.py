# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input("Введите число для преобразовывания десятичного числа в двоичное: "))

s = ""

while n != 0:
    s = str(n%2) + s
    n //=2

print(s)