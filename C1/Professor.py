from Person import Person
from log import Log

class Professor(Person):
    def __init__ (self, pName, pSurname, pAge, pnt, pPosition):
        super().__init__(pName, pSurname, pAge)
        self.nt = pnt
        self.position = pPosition
        self.sublist = []
        Log('CRE', 'создан ' + str(self))
        
    def setPosition(self, newPosition):
        self.position = newPosition
        Log('INF', 'добавлен ' + str(newPosition))

    def addSubj(self, newsubj):
        if newsubj not in self.sublist:
            self.sublist.append(newsubj)
            Log('INF', 'добавлен ' + str(newsubj))

    def delSubj(self, delsubj):
        if delsubj in self.sublist:
            self.sublist.remove(delsubj)
            Log('INF', 'удален ' + str(delsubj))


    def subjPrint(self):
        Log('INF', 'распечатан ' + str(self.sublist))
        return ', '.join(self.sublist)
        

    def __str__(self):
        retVal = "Имя = %s, Фамилия = %s, Возраст = %d, номер удостоверения = %d, Должность = %s" %(self.name, self.Surname, self.age, self.nt, self.position)
        Log('INF', 'распечатан ' + retVal)       
        return retVal
    

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
