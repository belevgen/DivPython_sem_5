# Задание 3
# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator()              # Пример использования
for i in range(10):
    print(next(fib_gen))
