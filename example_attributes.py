class Person:
    def __init__(self, name):                  # Вызывается при обращении Person()
        self._name = name                      # Вызовет __setattr__!
    
    def __getattr__(self, attr):               # Вызывается операцией obj.undefined
        if attr == 'name':                     # Для отсутствующего атрибута с именем name
            print('fetch...')
            return self._name                  # Не вызывает зацикливание: существующий атрибут
        else:                                  # Обращение к другим несуществующим
            raise AttributeError(attr)         # атрибутам вызывает ошибку

    def __setattr__(self, attr, value):        # Вызывается операцией obj.any = value
        if attr == 'name':
            print('change...')
            attr = '_name'
                                               # Внутреннее имя атрибута
        self.__dict__[attr] = value            # Предотвратить зацикливание

    def __delattr__(self, attr):               # Вызывается операцией del obj.any
        if attr == 'name':
            print('remove...')
            attr = '_name'
        
        del self.__dict__[attr]                # Предотвратить зацикливание, но менее обычным способом

bob = Person('Bob Smith')                      # Объект bob обладает управляемым атрибутом
print(bob.name)                                # Вызовет __getattr__
bob.name = 'Robert Smith'                      # Вызовет __setattr__
print(bob.name)                                # Вызовет __getattr__
del bob.name                                   # Вызовет __delattr__

print('_'*18)
sue = Person('Sue Jones')                      # Объект sue также наследует свойство
print(sue.name)
# print(Person.name.__doc__)                   # Не имеет эквивалента в данном случае