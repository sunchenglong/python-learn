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