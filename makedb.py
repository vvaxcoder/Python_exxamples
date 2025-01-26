from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=123456)
tom = Manager('Tom Jones', 51234)

import shelve

db = shelve.open('persondb') # file name

for object in (bob, sue, tom):
    db[object.name] = object

db.close()