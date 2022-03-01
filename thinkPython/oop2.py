# class Person:
#     def __init__(self, name, age=10):
#         # print(self, 'is generated')
#         self.name = name
#         self.age = age

# p1 = Person('Bob', 30)
# p2 = Person('Kate', 20)
# p3 = Person('Aaron')

# print(p1.name, p1.age, p2.name, p2.age, p3.name, p3.age)


#1. 숫자를 하나 증가
#2. 숫자를 0으로 초기화
# class Counter:
#     def __init__(self, num = 0) -> None:
#         self.num = num
#     def increment(self):
#         self.num += 1
#     def reset(self):
#         self.num = 0
#     def print_current_value(self):
#         print('현재값은: ', self.num)
# c1 = Counter()
# c1.print_current_value()
# c1.increment()
# c1.increment()
# c1.print_current_value()
# c1.reset()

# c2 = Counter()
# c2.print_current_value()

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))
    
    def sleep(self, minute):
        print('{}은 {}분 동안 잡니다.'.format(self.name, minute))
    
    def work(self, minute):
        print('{}은 {}분 동안 준비를 합니다.'.format(self.name, minute))

class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def work(self, minute):
        print('{}은 {}분 동안 공부합니다.'.format(self.name, minute))
class Employee(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def work(self, minute):
        super().work(minute)
        print('{}은 {}분 동안 업무를 합니다.'.format(self.name, minute))
bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)
