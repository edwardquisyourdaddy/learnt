class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))


class Animal(object):

    def run(self):
        print('Animal is running')


def run_twice(Animal):
    Animal.run()
    Animal.run()


class Dog(Animal):

    def run(self):
        print('Dog is running')


class Cat(Animal):

    def run(self):
        print('Cat is running')
