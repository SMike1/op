import string

"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""


def wiki_function():
    # Тело функции
    successful = string.ascii_uppercase + string.ascii_lowercase + " "
    text = []

    with open("text.txt", "r") as file:
        for line in file:
            line = "".join(list(filter(lambda x: x in successful, line))).lower()
            if line != "":
                text += line.split()

    line = " ".join(text)
    info = []
    for word in text:
        if not ([word, line.count(word)] in info):
            info.append([word, line.count(word)])

    info.sort(key=lambda x: x[1], reverse=True)

    word_count = dict()
    for index, item in enumerate(info):
        word_count[item[0]] = item[1]
        if index < 10:
            print(f"{index + 1} place --- {item[0]} --- {word_count[item[0]]} times")
            line = line.replace(" " + item[0] + " ", " PYTHON ")

    with open("new_text.txt", "w") as file:
        temp = ""
        for word in line.split():
            if len(temp) + len(word) < 100:
                temp += word + " "
            else:
                print(temp, file=file)
                temp = word + " "

    return 1

# Вызов функции
wiki_function()
