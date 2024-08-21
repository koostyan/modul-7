import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        last_modified_time = os.path.getmtime(filepath)
        last_modified_time_readable = time.ctime(last_modified_time)
        file_size = os.path.getsize(filepath)
        parent_directory = os.path.dirname(filepath)

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {last_modified_time}, Родительская директория: {parent_directory}')
