a = [x * x for x in range(1, 10)]
print a

b = [x * x for x in range(1, 10) if x % 2 != 0]
print b

L = ['Hello', 'World', 18, 'Apple', None]
print L

print [s.lower() for s in L if isinstance(s, str)]

m = (s.lower() for s in L if isinstance(s, str))
print m.next()
print str(m)


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


print [x for x in fib(30)]


def triangles():
    result = [1]
    while 1:
        yield result
        result = [sum(i) for i in zip([0] + result, result + [0])]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

from random import randint

nums = [randint(1, 10) for i in range(2)]
print nums
from operator import add

ans = add(*nums)
print ans

from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called ' % (ctime(), func.__name__)
        return func()

    return wrappedFunc


@tsfunc
def foo():
    pass


foo()
sleep(4)
for i in range(2):
    sleep(1)
    foo()


def convert(func, seq):
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 99999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)


def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    print 'formal arg1', arg1
    print 'formal arg2', arg2
    for eachXtrArg in theRest:
        print 'another arg', eachXtrArg


tupleVarArgs('abc')
tupleVarArgs(23, 4233.2)
tupleVarArgs('abc', 123, 45.5, 344, 'acxd')


def dictVarArgs(arg1, arg2='defaultB', **theRest):
    print 'formal arg1', arg1
    print 'formal arg2', arg2
    for key in theRest.keys():
        print 'Xtra arg %s: %s' % (str(key), str(theRest.get(key)))


dictVarArgs(1220, 74.0, c='abc')
dictVarArgs('abc', 'def', n='mmm', mfdsf='123')
