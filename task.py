class Person():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.surname = ""
            
    def setSurname(self, surname):
        self.surname = surname

    def printInfo(self):
        print(f"{self.name}, {self.nationality}")

    def getSurname(self):
        print(f"{self.surname}")


class Student(Person):
    def __init__(self, student_id, name, nationality):
        super().__init__(name, nationality)
        self.student_id = student_id

    def printInfo(self):
        print(f"{self.name}, {self.nationality}, {self.student_id}")


class Teacher(Person):
    def __init__(self, teacher_id, name, nationality):
        super().__init__(name, nationality)
        self.teacher_id = teacher_id

    def printInfo(self):
        print(f"{self.name}, {self.nationality}, {self.teacher_id}")


person1 = Person('Beket', "Kazakh")
person1.setSurname("Barlykov")
person1.printInfo()
person1.getSurname()
