from Person import Person
from log import Log

class Student(Person):
    def __init__ (self,  pName, pSurname, pAge, pST):
        super().__init__(pName, pSurname, pAge)
        self.st = pST
        self.eb = {}
        Log('CRE', 'создан ' + str(self))
        
    def addMark(self, subj, mark):
        self.eb[subj] = mark
        Log('INF', 'добавлен ' + str(subj))


    def getMark(self, subj):
        if subj in self.eb:
            Log('INF', 'распечатан ' + str(self.eb[subj]))
            return self.eb[subj]
        else:
            s = subj + ' not found'
            Log('ERR', s)
            raise ValueError(s)

    def formPrint(self):
        r = ', '.join(map(lambda x: str(x) + ' - ' + str(self.eb[x]), self.eb))
        Log('INF', 'распечатан ' + r)
        return r
            
    def __str__(self):
        s = "Имя = %s, Фамилия = %s, Возраст = %d, номер студенческого = %d" %(self.name,self.Surname,self.age,self.st)
        Log('INF', 'распечатан ' + s)
        return s

# Тесты
student1 = Student("Ярик", "Суслин", 18, 189234)
student1.addMark("Физика", 3)
student1.addMark("Математика", 5)
student1.addMark("Физ-ра", 4)
assert student1.getMark('Физика') == 3
assert student1.getMark('Математика') == 5
assert student1.getMark('Физ-ра') == 4
try:
    student1.getMark("Астрономия")
except ValueError as va:
    assert str(va) == "Астрономия not found"

assert student1.formPrint() == 'Физика - 3, Математика - 5, Физ-ра - 4'
assert str(student1) == 'Имя = Ярик, Фамилия = Суслин, Возраст = 18, номер студенческого = 189234'

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
