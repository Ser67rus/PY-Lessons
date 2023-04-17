"""
Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

Пример:
Ввод: 13 -> 1, 2, 4, 8
"""
N = int(input("Введите число N: "))
k = 0
while 2**k < N:
    k = k + 1
nums = [0] * k
k = 0
while 2**k < N:
    nums[k] = 2**k
    k = k + 1
print(f"{N} -> {nums}")