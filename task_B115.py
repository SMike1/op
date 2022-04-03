# Дано два слова и буква, вернуть одно слово, представляющее собой комбинацию обоих слов,
# слитых в той точке, где данная буква впервые появляется в каждом слове.
# Написать функцию string_merge, возвращающую строку, которое имеет начало
# первого слова и конец второго, с разделительной буквой в середине.
#
# Пример:
# string_merge("hello", "world", "l") ==> "held"

import traceback


def string_merge(string1, string2, letter):
    # Тело функции
    return ""


# Тесты
try:
    assert string_merge("hello", "world", "l") == "held"
    assert string_merge("coding", "anywhere", "n") == "codinywhere"
    assert string_merge("jason", "samson", "s") == "jasamson"
    assert string_merge("wonderful", "people", "e") == "wondeople"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
