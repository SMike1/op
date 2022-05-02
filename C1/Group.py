from Person import Person
from Student import Student
from Professor import Professor


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
            return self.ListGroup[index]


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
            else:
                f.write(str(person.subjPrint())+'\n'+'\n')
        f.close()

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
     
