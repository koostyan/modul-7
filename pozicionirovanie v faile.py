from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')  # Открываем файл в режиме записи

    try:
        for line_number, string in enumerate(strings, start=1):  # Получаем текущую позицию в файле перед записью строки
            byte_position = file.tell()  # Записываем строку в файл с добавлением новой строки
            file.write(string + '\n')  # Сохраняем информацию о позиции и строке в словаре
            strings_positions[(line_number, byte_position)] = string
    finally:
        file.close()  # Закрываем файл

    return strings_positions


file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
positions = custom_write(file_name, strings)

print(positions)
