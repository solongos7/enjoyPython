# a = 'abcdef\n'
# print(a)

# b = r'abcdef\n' #row string
# print(b)

import re

m = re.search(r'abc','123abdef')
# print(m.start())
# print(m.end())
# print(m.group())
# print(m)

r = re.search(r'\w+_(\w+유치원)_.+\.xlsx?', '광주광역시교육청_우정유치원_080325.xlsx')
print(r.group(1)) # 첫번째
print(r.group(0)) # 전체