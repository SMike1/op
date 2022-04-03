# Написать функцию sum_of_fractions, которая получает вещественное число и возвращает строку - сумму слагаемых числа в виде дробей. 
# Между слагаемыми поставить символ +, все отделить пробелами 
#
# Примеры:
# sum_of_fractions(1.24) ==> '1 + 2/10 + 4/100'

import traceback


def sum_of_fractions(num):
    # Тело функции
    return ""


# Тесты
try:
    assert sum_of_fractions(1.24) == '1 + 2/10 + 4/100'
    assert sum_of_fractions(7.304) == '7 + 3/10 + 4/1000'
    assert sum_of_fractions(0.04) == '4/100'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")