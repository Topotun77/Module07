from os import walk, path
from time import gmtime, strftime, localtime

for dir_, sub_dir, files in walk('.'):
    print('\n', dir_, sub_dir, files)
    for file_ in files:
        abs_dir = path.abspath(dir_)
        filepath = path.join(abs_dir, file_)
        filetime = path.getmtime(filepath)
        formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
        file_size = path.getsize(filepath)
        parent_dir = path.dirname(filepath)
        print(f'Обнаружен файл: {file_},\n\tПуть: {filepath},\n\tРазмер: {file_size} байт,\n\t'
            f'Время изменения: {formatted_time},\n\tРодительская директория: {parent_dir}')