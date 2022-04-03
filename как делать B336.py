# Написать функцию order, которая отсортирует заданную строку. Каждое слово в строке
# содержит одну цифру. Эта цифра - позиция, которую слово должно занимать в результате.
#
# Пример:
# order("is2 Thi1s T4est 3a")  ==>  "Thi1s is2 3a T4est"
# через split разбиваем список на массив(d) из слов,
# создаем массив с количеством элементов равным количеству слов(r),
# запускаем цикл по массиву (d) и в каждом элементе убираем все буквы из строки, оставляем число
# это число будет являтся в массиве r по которому нужно записать текущий элемент по массиву d
# c помощью join из списка  r сделать результирующую строку и вернуть её через return


import traceback


def order(sentence):
    # Тело функции
    return ""


# Тесты
try:
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("beli7eve Eve1rything if4 jus6t i2s y5ou 3possible") == "Eve1rything i2s 3possible if4 y5ou jus6t beli7eve"
    assert order("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
