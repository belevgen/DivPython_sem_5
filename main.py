# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
#
# Сформируйте словарь, где:
# второе и третье число являются ключами.
# первое число является значением для первого ключа.
# четвертое и все возможные последующие числа
#        хранятся в кортеже как значения второго ключа.

data = input('Введите строку из четырех и более чисел через "/": ')
first, second, third, *my_list = data.split('/')
my_dict = {int(second): int(first), int(third): tuple(map(int, my_list))}
print(my_dict)
print(f'{my_dict=}')

# 2
text = "сохраните в переменной строку текста"
my_dict = {}
for symbol in text:
    my_dict[symbol] = ord(symbol)
print(my_dict)

new_dict = {symbol: ord(symbol) for symbol in text}
print(f"{new_dict=}")

# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = "сохраните в переменной строку текста"
new_dict = {symbol: ord(symbol) for symbol in text}
my_iter = iter(new_dict.items())
count = 5
for _ in range(count):
    print(*next(my_iter))

# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
    # без перехода на новую строку.

LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMNS = 4

new_gen = (f'{k:>2} x {j:>2} = {k * j:>2}\t' if k != i + COLUMNS - 1
           else f'{k:>2} x {j:>2} = {k * j:>2}\n'
           for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMNS)
           for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
           for k in range(i, i + COLUMNS)
           )
print(*new_gen, end='')

######
LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMNS = 4

for i in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS):
    for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        for k in range(i, i + COLUMNS):
            if j * k == 50:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\n\n', end='')
            elif k != i + COLUMNS - 1:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\t', end='')
            else:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\n', end='')

# new_gen = (f'{k:>2} x {j:>2} = {k * j:>2}\n\n' if j * k == 50
#           else f'{k:>2} x {j:>2} = {k * j:>2}\t' if k != i + COLUMNS - 1
#           else f'{k:>2} x {j:>2} = {k * j:>2}\n'
#           for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMNS)
#           for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
#           for k in range(i, i + COLUMNS)
#           )
# print(*new_gen, end='')

# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится нацело только на единицу и на себя».