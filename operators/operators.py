# # operator if
# number = 23
# guess = int(input('Введите целое число:' ))

# if guess == number:
#     print('Числа равны');
# elif guess < number:
#     print('guess меньше')
# else: print('больше или иначе')


# # operator while
# number = 23
# running = True
# while running:
#     guess = int(input('Введите целое число : '))
#     if guess == number:
#         print('Поздравляю, вы угадали.')
#         running = False # это останавливает цикл while
#     elif guess < number:
#         print('Нет, загаданное число немного больше этого.')
#     else:
#         print('Нет, загаданное число немного меньше этого.')
# else: print('Цикл while закончен.')
# # Здесь можете выполнить всё что вам ещё нужно
# print('Завершение.')

# #cycle for
# for i in range(1,5):
#     print(i)
# else: print('Цикл окончен')

# # operator break
# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     print('Длина строки:', len(s))
# print('Завершение')

# operator continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
print('Введённая строка достаточной длинны')
