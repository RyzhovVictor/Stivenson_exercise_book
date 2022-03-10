"""Упражнение 10. Арифметика
(Решено. 22 строки)"""
# TODO Создайте программу, которая запрашивает у пользователя два целых числа a и b,
#  после чего выводит на экран результаты следующих математических операций:
# TODO  сумма a и b;
# TODO  разница между a и b;
# TODO  произведение a и b;
# TODO  частное от деления a на b;
# TODO  остаток от деления a на b;
# TODO  десятичный логарифм числа a;
# TODO  результат возведения числа a в степень b.
# TODO Подсказка. Функцию log10 вы найдете в модуле math.
from cmath import log10

user_input_a = int(input('Укажите первое число:'))
user_input_b = int(input('Укажите второе число:'))

print(user_input_a + user_input_b)
print(user_input_a - user_input_b)
print(user_input_a * user_input_b)
print(user_input_a / user_input_b)
print(user_input_a % user_input_b)
print(log10(user_input_a))
print(user_input_a ** user_input_b)
