import numpy as np

scores = np.array([[1, 1, 1, 1],
          [2, 2, 2, 2],
          [3, 3, 3, 3],
          [4, 4, 4, 4],
          [5, 5, 5, 5]])

y = np.array([0, 1, 2, 3, 3])
x = np.array([0, 1, 2, 3, 3])

ds = scores
# ind = np.zeros_like(scores)
# ind[np.arange(5), y] = 1
# ds -= ind
ds[range(5), y] -= 1

print(x.T.dot(y))


A = np.array([[1, 1], [1, 1], [1, 1]])
b = [1, 1, 1]

print (A.T.dot(b))
