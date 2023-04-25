"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии
"""
def inpower (a, b):
    if(b == 1):
        return a
    if( b != 1):
        return (a * inpower(a, b - 1))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
ans = inpower(a,b)

print(f"{a} ^ {b} = {ans}")

def sum (a,b):
    if(b == 1):
        return a + 1
    if (b != 1):
        return sum(a+1,b-1)

ans1 = sum(a,b)
print(f"{a} + {b} = {ans1}")