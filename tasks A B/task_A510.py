# Создать список (каталог мобильных приложений), состоящий из словарей (приложение). Словари должны содержать как минимум 5 полей
# (например, номер, название, рейтинг...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# apps = [{"id" : 123456, "title" : "Google Play", "rating" : 4.9,...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех приложениях;
# – вывода информации о приложении по введенному с клавиатуры номеру;
# – вывода количества приложений, с оценкой выше введённого;
# – обновлении всей информации о приложении по введенному номеру;
# – удалении приложения по номеру.
# Провести тестирование функций.
import traceback

apps =  [
        {"id" : 1, "title" : "BrawlStars", "rating" : 4.9, "size" : 115, "author": "Bib Dark"},
        {"id" : 2, "title" : "Instagram", "rating" : 4.5, "size" : 56, "author": "Rayan Gosling"},
        {"id" : 3, "title" : "Vkontakte", "rating" : 4, "size" : 76, "author": "Bread Pitta"},
        {"id" : 4, "title" : "TikTok", "rating" : 4.7, "size" : 89, "author": "Alan Wake"},
        {"id" : 5, "title" : "Steam", "rating" : 3, "size" : 38, "author": "Geyb Niuel"},
        {"id" : 6, "title" : "GosUslugi", "rating" : 2, "size" : 205, "author": "Alash Dursling"},
        {"id" : 7, "title" : "Spotify", "rating" : 3.6, "size" : 150, "author": "Vank Babe"},
        {"id" : 8, "title" : "WhatsApp", "rating" : 2.5, "size" : 46, "author": "Drake"},
        {"id" : 9, "title" : "Opera", "rating" : 1.5, "size" : 48, "author": "Asap"},
        {"id" : 10, "title" : "Telegram", "rating" : 4.6, "size" : 205, "author": "Pavel Durov"},
        ]
def All_apps(app):
    result = []
    for item in app:
        a = []
        for key in item:
            a.append(str(item[key]))
        result.append(' '.join(a))
    return '\n'.join(result)

    
def search_app_number(digit,items):
    resultApp = []
    for item in items:
        b = []
        if item["id"] == digit:
            for key in item:
                b.append(str(item[key]))
            resultApp.append(' '.join(b))    
            return '\n'.join(resultApp)
            break

    
def search_app_rating(rating,items):
    i = 0
    for item in items:
        if (item["rating"]) > rating:
            i +=1
    return i

        
def set_new_app_id(digit, items, new_digit, title, rating, size, author):
    for item in items:
        if item["id"] == digit:
            item["id"] = new_digit
            item["title"] = title
            item["rating"] = rating
            item["size"] = size
            item["author"] = author
            break

        
def pop_app_id(digit,items):
    for item in items:
        if item["id"] == digit:
            items.pop(items.index(item))
try:
    assert All_apps(apps) == '''1 BrawlStars 4.9 115 Bib Dark
2 Instagram 4.5 56 Rayan Gosling
3 Vkontakte 4 76 Bread Pitta
4 TikTok 4.7 89 Alan Wake
5 Steam 3 38 Geyb Niuel
6 GosUslugi 2 205 Alash Dursling
7 Spotify 3.6 150 Vank Babe
8 WhatsApp 2.5 46 Drake
9 Opera 1.5 48 Asap
10 Telegram 4.6 205 Pavel Durov'''
    assert search_app_number(1, apps) == '1 BrawlStars 4.9 115 Bib Dark'
    assert search_app_rating(3.9 , apps) == 5 
    set_new_app_id(1, apps, 2, "ClashRoyal", 3.5, 78, "Travis Scott")
    pop_app_id(6, apps)
    assert All_apps(apps) == '''2 ClashRoyal 3.5 78 Travis Scott
2 Instagram 4.5 56 Rayan Gosling
3 Vkontakte 4 76 Bread Pitta
4 TikTok 4.7 89 Alan Wake
5 Steam 3 38 Geyb Niuel
7 Spotify 3.6 150 Vank Babe
8 WhatsApp 2.5 46 Drake
9 Opera 1.5 48 Asap
10 Telegram 4.6 205 Pavel Durov'''
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")


