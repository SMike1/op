from Person import Person

class Professor(Person):
    def __init__ (self, pName, pSurname, pAge, pnt, pPosition):
        super().__init__(pName, pSurname, pAge)
        self.nt = pnt
        self.position = pPosition
        self.sublist = []
        
    def setPosition(self, newPosition):
        self.position = newPosition

    def addSubj(self, newsubj):
        if newsubj not in self.sublist:
            self.sublist.append(newsubj)

    def delSubj(self, delsubj):
        if delsubj in self.sublist:
            self.sublist.remove(delsubj)

    def subjPrint(self):
        return ', '.join(self.sublist)

    def __str__(self):
        return "Имя = %s, Фамилия = %s, Возраст = %d, номер удостоверения = %d, Должность = %s" %(self.name, self.Surname, self.age, self.nt, self.position)

# Тесты

professor1 = Professor("Иван", "Раков", 67, 32, "Decan")
assert str(professor1) == 'Имя = Иван, Фамилия = Раков, Возраст = 67, номер удостоверения = 32, Должность = Decan'

professor1.setPosition("Декан")
assert str(professor1) == 'Имя = Иван, Фамилия = Раков, Возраст = 67, номер удостоверения = 32, Должность = Декан'

professor1.addSubj("Математический анализ")
assert professor1.subjPrint() == 'Математический анализ'

professor1.addSubj("Математический анализ")
assert professor1.subjPrint() == 'Математический анализ'

professor1.addSubj("Геодезия")
assert professor1.subjPrint() == 'Математический анализ, Геодезия'

professor1.delSubj("Математический анализ")
assert professor1.subjPrint() == 'Геодезия'
