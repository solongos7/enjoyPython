class Person:
    def __init__(self, name, age=10):
        # print(self, 'is generated')
        self.name = name
        self.age = age

p1 = Person('Bob', 30)
p2 = Person('Kate', 20)
p3 = Person('Aaron')

print(p1.name, p1.age, p2.name, p2.age, p3.name, p3.age)

