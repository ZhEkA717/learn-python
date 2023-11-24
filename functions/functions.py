# def sayHello():
#     print('Hello world!')

# sayHello()

# def printMax(a,b):
#     print(max(a,b))

# printMax(1,3)

# var = 50

# def func(var):
#     print(var)
#     var = 2
#     print(var)

# func(5)

#global
# x = 50

# def func():
#     global x

#     print(x)

#     x = 2

#     print(x)

# func()

# print(x)

# #nonlocal
# def func_outer():
#     x = 2
#     print(x)

#     def func_inner():
#         nonlocal x
#         x = 5
#     func_inner()
#     print(x)

# func_outer();

# #Ключевые аргумент

# def func(a,b=5,c=10):
#     print(a,b,c)

# func(1)
# func(1,2,3)
# func(b=10, a = 1)
# func(c=222, a=12)

# #Переменное число параметров

# def total(a, *numbers, **phonebook):
#     print('a:', a)

#     #проход по элементам кортежа
#     for item in numbers:
#         print('item:', item)
    
#     #проход по элементам словаря
#     for key, value in phonebook.items():
#         print(key,':',value)

# print(total(10, 10, 11, 12, name="jack", age=18, id=1))

##Только ключевые параметры
# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)

# total(10, 1, 2, 3, extra_number=50)

# # total(10, 1, 2, 3)
# # Вызовет ошибку, поскольку мы не указали значение
# # аргумента по умолчанию для 'extra_number'.

#Строки документации

def func_doc():
    '''Строки документации'''
    
print(func_doc.__doc__)