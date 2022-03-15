from re import X
from tkinter import Y, YView


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)
        
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x, new_y)


p1 = Point(3, 4)
p2 = Point(2, 7)
p3 = p1 + p2

print(p1)
print(p2)
print(p3)