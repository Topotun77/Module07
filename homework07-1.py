file_ = 'poetry.txt'
fs = open(file_, 'r', encoding='utf8')
data_ = fs.read()
fs.close()
print(data_)