import pickle
from Person import Person
from Student import Student
from Professor import Professor
from Group import Group

with open("group.pkl", "rb") as f:
    group1 = pickle.load(f)
    assert len(group1) == 4
    assert str(group1) == '''1 группа
Имя = Иван, Фамилия = Раков, Возраст = 67, номер удостоверения = 32, Должность = Декан
Имя = Ярик, Фамилия = Суслин, Возраст = 18, номер студенческого = 189234
Имя = Slava, Фамилия = Lozkin, Возраст = 19, номер студенческого = 187632
Имя = Ваня, Фамилия = Пермский, Возраст = 18, номер студенческого = 111111
Имя = Кирилл, Фамилия = Мирный, Возраст = 18, номер студенческого = 189801'''

