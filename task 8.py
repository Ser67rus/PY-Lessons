"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
Числа вводятся построчно.
"""
n = int(input("Введите длину шоколадки в дольках: "))
m = int(input("Введите ширину шоколадки в дольках: "))
k = int(input("Введите желаемое количество долек: "))

if ((k%n == 0) or (k%m == 0)) and (n*m >= k):
    print('%i, %i, %i -> yes'%(n,m,k))
else:
    print('%i, %i, %i -> no'%(n,m,k))
