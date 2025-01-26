class SkipIterator:
    def __init__(self, wrapped) -> None:
        self.wrapped = wrapped               # Информация о состоянии
        self.offset = 0
    
    def next(self):
        if self.offset >= len(self.wrapped): # Завершить итерации
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # Иначе перешагнуть и вернуть
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped) -> None:     # Сохранить используемый элемент
        self.wrapped = wrapped
    
    def __iter__(self):
        return SkipIterator(self.wrapped)    # Каждый раз новый итератор
    
if __name__ == '__main__':
    alpha = 'wsfdvdfgmnjhk'
    skipper = SkipObject(alpha)              # Создать объект-контейнер
    I = iter(skipper)                        # Создать итератор для него
    print(next(I), next(I), next(I))         # Обойти элементы 0, 2, 4

    for x in skipper:                        # for вызывает __iter__ автоматически
        for y in skipper:                    # Вложенные циклы for также вызывают __iter__
            print(x + y, end=' ')            # Каждый итератор помнит свое состояние, смещение