s1 = 'Sweet Coder'
s2 = "I'm a bad joker"
s3 = "C:\\Windows\\temp\\network\\new_file.txt"
s4 = """hello "world"!!! """
print(s3)
print(s4)

age = 26
name = 'Swaroop'
print('Возраст {0} -- {1} лет.'.format(name, age))

print('Почему {0} забавляется с этим Python?'.format(name))

# Python » PEP Index » PEP 3101Toggle light / dark / auto colour theme
# PEP 3101 – Advanced String Formatting
# https://peps.python.org/pep-3101/

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{:.3}'.format(1/3)) #-> 0.333

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{:_^11}'.format('hello')) #-> ___hello___

# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
#->'Swaroop написал A Byte of Python'
