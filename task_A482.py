# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback


def palindrome(num):
    x=0
    for i in range(1,num):
        x =+1
        print(i)
    return []


# Тесты
try:
    assert palindrome(1551) == [55, 1551]
    assert palindrome(221122) == [11, 22, 2112, 221122]
    assert palindrome(10015885) == [88, 1001, 5885]
    assert palindrome(13598) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
