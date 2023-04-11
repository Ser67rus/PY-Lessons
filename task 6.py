"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

"""
while True:
    inp_data = int(input("Введите шестизначный номер билета: "))

    if inp_data//10**6 > 0:
        print("введенное число не шестизначное")
    elif inp_data//10**(6-1) == 0:
        print("введенное число не шестизначное")
    else:
        break

counter = inp_data
result1 = 0
result2 = 0
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

while counter > 999:
    result1 = result1 + counter//(10**(size-1))
    counter = counter % (10**(size-1))
    size = size - 1
while counter > 0:
    result2 = result2 + counter//(10**(size-1))
    counter = counter % (10**(size-1))
    size = size - 1
if result1 == result2:
    print('%i -> yes'%inp_data)
else:
    print('%i -> no'%inp_data)
