def generate():                  # Терпит неудачу при выполнении под управлением
    class Spam:                  # Python до версии 2.2
        count = 1

        def method(self):                  # Имя Spam недоступно:
            # print(Spam.count)            # Не локальное (def), не глобальное (модуль), не встроенное
            print(self.__class__.count)    # Работает: используется атрибут для получения класса
    return Spam()

generate().method()