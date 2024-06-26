# Ссылка на GitHub с этим же кодом:
# https://github.com/Topotun77/Module07/blob/master/homework07-2.py
#
# Вопрос: Чем отличается использование оператора with open(file_name...)
# от простого использования file.close()?
#
# Ответ: with open(file_name...) предпочтительнее использовать, т.к. в этой конструкции
# произойдет автоматическое закрытие файла даже если внутри блока между открытием
# и закрытием файла возникнет какая-то непредвиденная ситуация.

file_ = 'poetry.txt'
with open(file_, 'r', encoding='utf8') as fs:
    data_ = fs.read()
print(data_)