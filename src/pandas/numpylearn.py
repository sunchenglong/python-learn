import numpy as np

a = np.arange(15).reshape(3, 5)
print a
print a.shape

print a.ndim
print a.dtype.name
print a.itemsize
print a.size
print type(a)
b = np.array([6, 7, 8])
print type(b)
print b.itemsize
print b.size

c = np.array([1, 2, 3, 4.1])
print type(c)
print c.dtype

d = np.array([(1, 2), (3, 4), (5, 6)])
print d.dtype
print d.itemsize
print d.ndim
print d.shape

e = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print e

print np.zeros((3, 4))
print np.ones((2, 3, 4), dtype=np.int16)
print np.empty((2, 3))

print np.arange(10, 30, 5)
print np.arange(0, 2, 0.3)

print np.linspace(0, 2, 9)

from numpy import pi

x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)
print f

import matplotlib.pyplot as plt

plt.plot(x, f)
# plt.show()

a = np.arange(6)
print a

b = np.arange(12).reshape(4, 3)
print b

c = np.arange(24).reshape(2, 3, 4, 1, 1)
print c

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])

print a.dot(b)
print np.dot(a, b)
print a * b

a = np.random.random((2, 3))
print a

b = np.ones((2, 3), dtype=int)
b *= 3
print b

a += b
print a

print a.sum()
print a.min()
print a.max()

a = np.arange(12).reshape(3, 4)
print a
print a.sum(axis=0)
print a.min(axis=1)
print a.cumsum(axis=1)

print np.exp(a)
print np.sqrt(np.exp(a))
print np.add(np.exp(a), np.sqrt(np.exp(a)))

print a
a = np.arange(10) ** 3
print a
print a[2:5]
a[:6:2] = -1000
print a
print a[::-1]

for i in a:
    print (i ** (1 / 3.))


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print b
print b[2, 3]
print b[0:5, 1:2]
print b[-1]
print b[:, -1]
print b.shape
for row in b:
    print b
for element in b.flat:
    print element

a = np.floor(10 * np.random.random((3, 4)))
print a
print a.shape

print a.flat
print a.ravel()
print a.reshape(1, 12)
print a
print a.reshape(2, -1)

c = np.array([[[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]])
print c.shape

print c[1, ...]
print c[1, :, :]

print c[..., 2]

a = np.floor(10 * np.random.random((2, 2)))
print a
b = np.floor(10 * np.random.random((2, 2)))
print b
vs = np.vstack((a, b))
print vs.shape
print vs
hs = np.hstack((a, b))
print hs.shape
print hs

cs = np.column_stack((a, b))
print cs.shape
print cs
print cs[1, :]
print cs[:, 1]
from numpy import newaxis

print cs[:, newaxis]

print np.r_[1:4, 0, 4]


def f(x):
    print(id(x))


a = np.arange(12)

print id(a)
f(a)

c = a.view()
print c
print c is a
print c.base is a
print a.base is a

a = np.arange(12) ** 2
print a
i = np.array([1, 1, 3, 8, 5])
print a[i]

j = np.array([[3, 4], [9, 7]])
print a[j]

palette = np.array([[0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])
image = np.array([[0, 1, 2, 0],
                  [0, 3, 4, 0]])
print palette[image]

a = np.arange(12).reshape(3, 4)
print a

i = np.array([[0, 1],
              [1, 2]])
j = np.array([[2, 1],
              [3, 3]])
print a[i, j]

print a[i, 2]

print a[:, j]
