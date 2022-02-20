# class Singer:
#     def sing(self):
#         return 'Lalala~'


# taeji = Singer()
# result = taeji.sing()
# print(result)
import diablo2

class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    # 먹고 자고 이야기하고...
    def eat(self):
        print('얌냠...')

    def sleep(self):
        print('쿨쿨...')

    def talk(self):
        print('주절주절...')

class Student(Person): # Person 클래스를 상속받음
    def study(self):
        print('열공열공...')    

jane = diablo2.Amazon()
mary = diablo2.Amazon()

print(jane.strength)
jane.exercise()
print(jane.strength)

lee = Person()
lee.talk()
kim = Student()
kim.talk()
kim.study()
