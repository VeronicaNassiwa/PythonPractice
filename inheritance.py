class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

personobj=Person("vero",27,"kitende")
#print(x.name)
#print(x.address)

class student(Person):
    def __init__(self,name,age,address,session):
        self.session=session
        super().__init__(name,age,address)

studOBJ=student("hussein",27,"kibuli","Evening")

print(studOBJ.address)


