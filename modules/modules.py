import sys

# # for i in sys.argv:
# #     print(i)

# print(sys.argv)

# # print(sys.path)

# import os

# print(os.getcwd)

# print(sys.__name__)


# if __name__ == '__main__':
#     print('Эта программа запущена сама по себе.')
# else:
#     print('Меня импортировали в другой модуль.')

# import mymodule

# mymodule.sayHi()

# print(mymodule.__version__)

# from mymodule import sayHi, __version__

# sayHi()

# print('Version', __version__)

from mymodule import *

# Это импортирует все публичные имена, такие как sayhi, но не импортирует
# __version__, потому что оно начинается с двойного подчёркивания

# import this 
var_a = 45
# print(dir(sys)) #-> возвращает список атрибутов модуля sys

# print(dir()) #-> по умолчанию возвращает список атрибутов текущего модуля


del var_a

# print(dir(str))
print(help(int))


