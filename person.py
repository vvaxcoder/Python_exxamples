class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self) -> str:
        return '[Pesrson: %s, %s]' % (self.name, self.pay)
    
class Manager(Person):
    def __init__(self, name, job=None, pay=0):
        super().__init__(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

class Department:
    def __init__(self, *args) -> None:
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    # print(bob)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.10)
    # print(sue)
    tom = Manager('Tom Riddle', pay=50000)
    # tom.giveRaise(.10)
    # print(tom.lastName())
    # print(tom)
    # print('--All three--')
    for object in (bob, sue, tom):
        object.giveRaise(.33)
        print(object)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.11)
    development.showAll()