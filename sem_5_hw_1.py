# Задание 1
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    file_name = os.path.basename(file_path)         # Используем os.path.basename для получения имени файла
    name, extension = os.path.splitext(file_name)   # Используем os.path.splitext для разделения имени файла и расширения
    file_dir = os.path.dirname(file_path)           # Используем os.path.dirname для получения пути до файла
    return file_dir, name, extension
file_path = "/path/to/your/file.txt"                # Пример использования функции
result = split_file_path(file_path)
print(result)
