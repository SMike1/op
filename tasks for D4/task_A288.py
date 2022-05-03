# Задан список положительных чисел arr и положительное число newavg.
# Написать функцию new_avg(arr, newavg), которая возвращает наименьшее целое число,
# которое нужно добавить к списку, чтобы среднее значение было больше или равно newavg
#
# Пример:
# new_avg([14, 30, 5, 7, 9, 11, 15], 30) ==> 149


import traceback


def new_avg(arr, newavg):
    return (newavg*(len(arr)+1)-sum(arr))


# Тесты
try:
    assert new_avg([14, 30, 5, 7, 9, 11, 15], 30) == 149
    assert new_avg([14, 30, 5, 7, 9, 11, 16], 90) == 628
    assert new_avg([14, 30, 5, 7, 9, 11, 15], 92) == 645
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
