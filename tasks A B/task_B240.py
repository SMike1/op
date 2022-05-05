# Написать функцию sum_of_fractions, которая получает вещественное число и возвращает строку - сумму слагаемых числа в виде дробей. 
# Между слагаемыми поставить символ +, все отделить пробелами 
#
# Примеры:
# sum_of_fractions(1.24) ==> '1 + 2/10 + 4/100'

import traceback


def sum_of_fractions(num):    
    list1 = str(num).split('.')
    res = []
    if list1[0] != '0':
        res.append(list1[0])
    a = 10
    for i in range(0, len(list1[1])):
        b = list1[1][i:i+1:1]
        if b != '0':
            res.append(b + '/' + str(a))        
        a = a * 10
    return ' + '.join(res)


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
