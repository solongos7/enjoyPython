class Time:
    '''시간을 표현'''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '시간을 표현하는 클래스'

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))



time = Time(9, 45, 30)
time.print_time()
print(time)

# print_self(start)
# start.print_time()