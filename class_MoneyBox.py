"""
класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
"""
class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.max = capacity

    def can_add(self, v):
        if self.count + v <= self.max:
            return(True)
        else: return(False)

    def add(self, v):
        if self.can_add(v) == True:
            self.count = self.count + v
