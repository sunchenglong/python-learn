a = lambda x, y: x + y
print a(3, 4.1)

print a(3, 5)
print a('abc', 'def')

b = lambda *z: z

print b(1, 23, 4.5, 'easf')

from random import randint


def odd(n):
    return n % 2


allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(odd, allNums)

from random import randint as ri

print [n for n in [ri(1, 99) for i in range(9)] if n % 2]

print map((lambda x: x + 2), range(1, 10))
print map((lambda x: x ** 2), range(6))
print [x + 2 for x in range(1, 10)]
print [x ** 2 for x in range(6)]

print map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])
print map(lambda x, y: (x + y, x - y), [1, 3, 5], [5, 3, 4])
print zip([1, 3, 5], [2, 4, 6])
print map(None, [1, 3, 5], [2, 4, 6])


def mySum(x, y): return x + y


allNums = range(5)
total = 0
for eachNum in allNums:
    total = mySum(total, eachNum)
print total

print reduce((lambda x, y: x + y), allNums)

from operator import add, mul
from functools import partial

add1 = partial(add, 1)
mul100 = partial(mul, 100)
print add1(10)
print add1(10)
print mul100(10)
print mul100(500)

print int('1001', base=2)
baseTwo = partial(int, base=2)
print baseTwo('10010101101')

from functools import partial
import Tkinter

root = Tkinter.Tk()
Mybutton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = Mybutton(text='Button 1')
b2 = Mybutton(text='Button 2')
qb = Mybutton(text='QUIT', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFas!')
root.mainloop()