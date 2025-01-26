from typing import Any


class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname: str, value: Any) -> None:
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self) -> None:
        self.__dict__['name'] = 'Gebbels'

x = Test1()
y = Test2()

x.name = 'Sasha'
y.name = 'Valya'

x.age = 31
y.age = 33