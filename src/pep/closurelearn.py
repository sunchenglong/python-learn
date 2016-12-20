def foo():
    bar = 200
    print "in foo bar is : ", bar


bar = 1000
print "in main bar is: ", bar
foo()
print "in main bar is(still): ", bar


def foo2():
    m = 3

    def bar():
        n = 4
        print m + n


print foo2()


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


count = counter(5)
print count()
print count()
count2 = counter(100)
print count2()
print count2()

output = '<int %r id = %0x val = %d>'
w = x = y = z = 1


def f1():
    x = y = z = 2

    def f2():
        y = z = 3

        def f3():
            z = 4
            print output % ('w', id(w), w)
            print output % ('x', id(x), x)
            print output % ('y', id(y), y)
            print output % ('z', id(z), z)

        clo = f3.func_closure
        if clo:
            print "f3 closure vars: ", [str(c) for c in clo]
        else:
            print "no f3 closure vars"
        f3()

    clo = f2.func_closure
    if clo:
        print "f2 closure vars: ", [str(c) for c in clo]
    else:
        print "no f2 closure vars"
    f2()


clo = f1.func_closure
if clo:
    print "f1 closure vars: ", [str(c) for c in clo]
else:
    print "no f1 closure vars"
f1()

from time import time, sleep


def logged(when):
    def log(f, *args, **kwargs):
        print '''Called
        function: %s
        args: %r
        kargs: %r
        ''' % (f, args, kwargs)

    def pre_logged(f):
        def wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)

        return wrapper

    def post_logged(f):
        def wrapper(*args, **kwargs):
            now = time()
            try:
                f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print "time delta: %s" % (time() - now)

        return wrapper

    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'


@logged("post")
def hello(name):
    print "Hello,", name
    sleep(4)


hello('world')
