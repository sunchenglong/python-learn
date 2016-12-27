def myfunc():
    print "myfunc() called"


myfunc()
myfunc()


def deco(func):
    print " before myfunc() called"
    func()
    print " after myfunc() called"
    return func


myfunc1 = deco(myfunc)

myfunc1()
myfunc1()


def deco(func):
    def _deco():
        print " before myfunc() called"
        func()
        print " after myfunc() called"

    return _deco


@deco
def myfunc1():
    print "myfunc1() called"
    return 'ok'


myfunc1()
myfunc1()


def deco(func):
    def _deco(a, b):
        print " before myfunc() called"
        ret = func(a, b)
        print " after myfunc() called, result is %s" % ret

    return _deco


@deco
def myfunc2(a, b):
    print "myfunc2() called"
    return a + b


myfunc2(1, 2)
myfunc2('abc', 'def')


def deco1(func):
    def _deco(*args, **kwargs):
        print " before %s called" % func.__name__
        ret = func(*args, **kwargs)
        print " after %s called, result is" % func.__name__, ret
        return ret

    return _deco


@deco1
def myfunc3(a, b):
    print "myfunc3() called"
    return a + b


@deco1
def myfunc4(a, b, c):
    print "myfunc4() called"
    return a + b + c


myfunc3(1, 3)
myfunc4('ab', 'cd', '###')
y = [1, 2, 3]
print [[_] for _ in y]


