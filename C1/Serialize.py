import pickle
from Person import Person
from Student import Student
from Professor import Professor
from Group import Group

professor1 = Professor("Иван", "Раков", 67, 32, "Decan")
professor1.setPosition("Декан")
professor1.addSubj("Математический анализ")
professor1.addSubj("Математический анализ")
professor1.addSubj("Геодезия")

student1 = Student("Ярик", "Суслин", 18, 189234)
student1.addMark("Физика", 3)
student1.addMark("Математика", 5)
student1.addMark("Физ-ра", 4)

student2 = Student("Slava", "Lozkin", 19, 187632)
student2.addMark("Физика", 4)
student2.addMark("ИЗО", 4)
student2.addMark("Физика", 3)

student3 = Student("Ваня", "Пермский", 18, 111111)
student3.addMark("Линейная алгебра", 5)
student3.addMark("Музыка", 4)
student3.addMark("Физика", 3)

student4 = Student("Кирилл", "Мирный", 18, 189801)
student4.addMark("Линейная алгебра", 5)
student4.addMark("Физ-ра", 4)
student4.addMark("Физика", 5)

group1 = Group(1)
group1 = group1 + professor1
group1 = group1 + student1
group1 = group1 + student2
group1 = group1 + student3
group1 = group1 + student4

r = pickle.dump(group1, open("group.pkl", "wb"))
print(r)





