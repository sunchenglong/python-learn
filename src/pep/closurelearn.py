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