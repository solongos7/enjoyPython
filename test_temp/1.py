# aaa = list('abcdefg')
# print(*aaa) #unpacking

import numpy as np

# x = [[50, 3],[21, 15],[32, 80]]
# y = [10,10]
# np_x = np.array(x)
# np_y = np.array(y)
# print(2*(np_x + np_y))
# np.column_stack()

a = np.array((1,2,3))
b = np.array((2,3,4))
print(np.column_stack((a,b)))
# [[1 2]
#  [2 3]
#  [3 4]]
print(np.row_stack((a, b)))
# [[1 2 3]
#  [2 3 4]]

z = 'regulation'
print(z.replace('a', '/'))

print('6'*(2**2))

np_heights = np.array([[1.75,1.65,1.8,1.5],[1.56,1.70,1.4,1.29],[1.49,1.68,1.3,1.8]])
np.sort(np_heights[0])
# print(np_heights[:, 0])
print(np.median(np_heights[:,0]))