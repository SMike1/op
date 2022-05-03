from Person import Person
from Student import Student
from Professor import Professor
from log import Log


class Group:
    def __init__(self, pNGroup):
        self.Ngroup = pNGroup
        self.ListGroup = []
        Log('CRE', 'создан ' + str(self))

    def __str__(self):
        s = str(self.Ngroup)+ " группа" + '\n' + '\n'.join(map(lambda x: str(x), self.ListGroup))
        Log('INF', 'распечатан ' + s)
        return s
 

    def __len__(self):
        if len(self.ListGroup) == 0:
            Log('INF', 'распечатан ' + 0)
            return 0
        else:
            s = len(self.ListGroup)-1
            Log('INF', 'распечатан {0}'.format(s))
            return s

    def getByIndex(self, index):
        if index <= len(self.ListGroup):
            s = self.ListGroup[index]
            Log('INF', 'распечатан {0}'.format(str(s)))
            return s
        else:
            s = 'index {0} out of bounds, group has {1} persons'.format(index, str(len(self.ListGroup)))
            Log('ERR', s)
            raise ValueError(s)            


    def setByIndex(self, index, person):
        if not (isinstance(person, Student) or isinstance(person, Professor)):
            s = 'person must be of type Student or Professor'
            Log('ERR', s)
            raise ValueError(s)
        if index > len(self.ListGroup) or index < 0:
            s = 'index out of bounds, group has ' + str(len(self.ListGroup)) + ' persons'
            Log('ERR', s)
            raise ValueError(s)
        if isinstance(person, Student) and index < 1:
            s = "Student must be at index 1 or higher"
            Log('ERR', s)
            raise ValueError(s)
        elif isinstance(person, Professor) and index != 0:
            s = "Professor must be at index 0"
            Log('ERR', s)
            raise ValueError(s)
        self.ListGroup[index] = person

    def __add__(self,other):
        self.ListGroup.append(other)
        Log('INF', 'добавлен ' + str(other))
        return self

    def delByIndex(self, index):
        if (index <= len(self.ListGroup)) and (index >= 0) :
            self.ListGroup.pop(index)
            Log('INF', 'удален person at index ' + str(index))
        else:
            s = 'index {0} out of bounds, group has {1} persons'.format(index, str(len(self.ListGroup)))
            Log('ERR', s)
            raise ValueError(s)  

    def infoToTxtFile(self):
        try:
            with open('newtext.txt' ,'w') as f:
                f.write(str(self.Ngroup) + ' группа\n')
                for person in self.ListGroup:
                    f.write(str(person) + '\n')
                    if isinstance(person, Student):
                        f.write(str(person.formPrint())+'\n'+'\n')
                    else:
                        f.write(str(person.subjPrint())+'\n'+'\n')
        except OSError as e:
            Log('ERR', str(e))
            sys.exit()

# Тесты

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

try:
    group1.setByIndex(10, student1)
except ValueError as va:
    assert str(va) == "index out of bounds, group has 5 persons"

try:
    group1.setByIndex(1, Person("Иван", "Драгов", 23))
except ValueError as va:
    assert str(va) == "person must be of type Student or Professor"

try:
    group1.setByIndex(2,professor1)
except ValueError as va:
    assert str(va) == "Professor must be at index 0"
    
try:
    group1.setByIndex(0,student1)
except ValueError as va:
    assert str(va) == "Student must be at index 1 or higher"

assert len(group1) == 4


assert str(group1.getByIndex(2)) == 'Имя = Slava, Фамилия = Lozkin, Возраст = 19, номер студенческого = 187632'
group1.delByIndex(2)
assert str(group1.getByIndex(2)) == 'Имя = Ваня, Фамилия = Пермский, Возраст = 18, номер студенческого = 111111'

assert str(group1) == '''1 группа
Имя = Иван, Фамилия = Раков, Возраст = 67, номер удостоверения = 32, Должность = Декан
Имя = Ярик, Фамилия = Суслин, Возраст = 18, номер студенческого = 189234
Имя = Ваня, Фамилия = Пермский, Возраст = 18, номер студенческого = 111111
Имя = Кирилл, Фамилия = Мирный, Возраст = 18, номер студенческого = 189801'''


group1.infoToTxtFile()
     
