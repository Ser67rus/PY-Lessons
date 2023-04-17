"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. С клавиатуры вводятся число монет и сами монеты построчно.
Пример:
Ввод: 1 1 1 1 0 0 -> 2
"""
coin_count = int(input("Введите количество монет: "))
coins =  [0] *coin_count
head_count = 0
tail_count = 0
for i in range(coin_count):
    while True:
        coins[i] = int(input("Введите сторону монеты (1/0): "))
        if ((coins[i] == 0) or (coins[i] == 1)):
            break
    if (coins[i] == 0):
        tail_count = tail_count + 1
    if (coins[i] == 1):
        head_count = head_count + 1

if (head_count > tail_count):
    print(f"{coins} -> {tail_count}")
else:
    print(f"{coins} -> {head_count}")

