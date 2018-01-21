# -*- coding: UTF-8 -*-
class cat:
    age = 10

    def __init__(self, color):
        self.color = color
        cat.age += 1

    def say(self):
        print(str(cat.age) + self.color)
        print(self)
        print(self.__class__)


class dog(cat):
    def __init__(self, male):
        self.male = male
        cat.__init__(self, 'green')


d = dog('male')
d.say()
print(d.age)
