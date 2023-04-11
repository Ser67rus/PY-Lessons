"""
Найдите сумму цифр трехзначного числа.
"""

while True:
    inp_data = int(input("Введите трехзначное число: "))

    if inp_data//1000 > 0:
        print("введенное число не трехзначное")
    elif inp_data//100 == 0:
        print("введенное число не трехзначное")
    else:
        break

counter = inp_data
result = 0
size = 0
a = 0
b = 1
while True:
    if inp_data//b == 0:
        break
    else:
        size = size + 1
        b = b * 10

while counter > 0:
    result = result + counter//(10**(size-1))
    counter = counter % (10**(size-1))
    size = size - 1
print('%i -> %i'%(inp_data, result))