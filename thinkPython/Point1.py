from math import sqrt


class Point:
    '''2차원 공간에 점을 표현한다.'''

class Rectangle:
    ''' 사각형을 표현한다.
        속성: width, height, corner
    '''

def print_point(p):
    print('(%g, %g)' %(p.x, p.y))

# def distance_between_points(p1, p2):
#     distance = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
#     print('%.2f' %distance)

# p1 = Point()
# p2 = Point()
# p1.x = 3.0
# p1.y = 4.0
# p2.x = 4.0
# p2.y = 5.0

# print_point(p1)
# print_point(p2)
# distance_between_points(p1, p2)

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)
