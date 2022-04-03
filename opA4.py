# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback

def len_num(num):
    lenn = 0
    while num>0:
        num = num // 10
        lenn = lenn + 1
    return lenn

def is_pol(num):
    if num < 10:
        return False
    n = num
    rev = 0
    while(n>0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return num == rev
#длина числа минус длина окна(i) + 1

def palindrome(num):
    q = set()
    nl = len_num(num)
    for i in range (2,nl+1):
        n = num
        for j in range(0,nl-i+1):
            r = n%(10**i)
            n = n // 10
            if is_pol(r):
                q.add(r)
    return sorted(q)


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
