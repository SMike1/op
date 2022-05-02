from Person import Person

class Student(Person):
    def __init__ (self,  pName, pSurname, pAge, pST):
        super().__init__(pName, pSurname, pAge)
        self.st = pST
        self.eb = {}
        
    def addMark(self, subj, mark):
        self.eb[subj] = mark

    def getMark(self, subj):
        if subj in self.eb:
            return self.eb[subj]
        else:
            raise ValueError(subj + ' not found')

    def formPrint(self):
        return ', '.join(map(lambda x: str(x) + ' - ' + str(self.eb[x]), self.eb))
            
    def __str__(self):
        return "Имя = %s, Фамилия = %s, Возраст = %d, номер студенческого = %d" %(self.name,self.Surname,self.age,self.st)

#Тесты
student1 = Student("Ярик", "Суслин", 18, 189234)
student1.addMark("Физика", 3)
student1.addMark("Математика", 5)
student1.addMark("Физ-ра", 4)
assert student1.getMark('Физика') == 3
assert student1.getMark('Математика') == 5
assert student1.getMark('Физ-ра') == 4

assert student1.formPrint() == 'Физика - 3, Математика - 5, Физ-ра - 4'
assert str(student1) == 'Имя = Ярик, Фамилия = Суслин, Возраст = 18, номер студенческого = 189234'

