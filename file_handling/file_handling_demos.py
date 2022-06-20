file_path = './new_text'

print('-------Whole file---------')
file = open(file_path, 'r')
print(file.read())

print('-------By bytes count---------')
file = open(file_path, 'r')
print(file.read(2))
print(file.read(3))
print(file.read(4))
