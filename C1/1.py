class Person:
    def __init__ (self, pName, pSurname, pAge):
        self.name = pName
        self.Surname = pSurname
        self.age = pAge

        
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
        return "Name = %s, Surname = %s, Age = %d, ST = %d" %(self.name,self.Surname,self.age,self.st)


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

    def __str__(self):
        return "Name = %s, Surname = %s, Age = %d, NT = %d, Position = %s" %(self.name, self.Surname, self.age, self.nt, self.position)    


class Group:
    def __init__(self, pNGroup):
        self.Ngroup = pNGroup
        self.ListGroup = []

    def __str__(self):
        return str(self.Ngroup)+ " группа" + '\n' + '\n'.join(map(lambda x: str(x), self.ListGroup))
 

    def __len__(self):
        if len(self.ListGroup) == 0:
            return 0
        else:
            return len(self.ListGroup)-1

    def getByIndex(self, index):
        if index <= len(self.ListGroup):
            print(self.ListGroup[index])


    def setByIndex(self, index, person):
        if not (isinstance(person, Student) or isinstance(person, Professor)):
            raise ValueError('person must be of type Student or Professor')
        if index < len(self.ListGroup) or index < 0:
            raise ValueError('index out of bounds, group has ' + str(len(self.ListGroup))) + ' persons'
        if isinstance(person, Student) and index < 1:
            raise ValueError("Student must be at index 1 or higher")
        elif isinstance(person, Professor) and index != 0:
            raise ValueError("Professor must be at index 0")
        self.ListGroup[index] = person

    def __add__(self,other):
        self.ListGroup.append(other)
        return self

    def delByIndex(self, index):
        if (index <= len(self.ListGroup)) and (index >= 0) :
            self.ListGroup.pop(index)

    def infoToTxtFile(self):
        f = open('newtext.txt' ,'w')
        f.write(str(self.Ngroup) + ' группа\n')
        for person in self.ListGroup:
            f.write(str(person) + '\n')
            if isinstance(person, Student):
                f.write(str(person.formPrint())+'\n'+'\n')
        f.close()
        
# tests
student1 = Student("Вася", "Пупкин", 18, 101)
student1.addMark("Физика", 5)
student1.addMark("ИЗО", 3)
student1.addMark("Мат. анализ", 4)
assert student1.getMark("Физика") == 5
try:
    student1.getMark("Астрономия")
except ValueError as va:
    assert str(va) == "Астрономия not found"
print(student1.formPrint())
print(student1)

Professor1 = Professor("Иван", "Раков", 67, 32, "Decan")
Professor1.setPosition("Декан")
Professor1.addSubj("Математический анализ")
Professor1.addSubj("Математический анализ")
print(Professor1)
Professor1.addSubj("Геодезия")
Professor1.delSubj("Математический анализ")
print(Professor1)

student2 = Student("Slava", "Lozkin", 19, 132)
student2.addMark("Физика", 4)
student2.addMark("ИЗО", 4)

student3 = Student("Ваня", "Пермский", 18, 111)
student3.addMark("Линейная алгебра", 5)
student3.addMark("Музыка", 4)


group1 = Group(1)
group1 = group1 + Professor1
group1 = group1 + student1
group1 = group1 + student2
group1 = group1 + student3
assert len(group1) == 3

group1.delByIndex(2)
group1.getByIndex(2)

# group1.setByIndex(1, student1)
#group1.setByIndex(0, Professor1)

group1.infoToTxtFile()

#group1.getByIndex(2)
#group = group + student1





