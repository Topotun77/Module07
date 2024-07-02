# Домашнее задание по теме "Позиционирование в файле".
# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
# Написать усовершенствованную функцию записи.
#
# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name -
# название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала
# строки>), а значением - записываемая строка. Для получения номера байта начала строки
# используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf8') as fs:
        for i in range(len(strings)):
            pos = fs.tell()
            fs.write(strings[i] + '\n')
            strings_positions[(i+1, pos)] = strings[i]
    fs.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)