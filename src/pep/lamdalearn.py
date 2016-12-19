
a = lambda x, y: x + y
print a(3,4.1)

print a(3,5)
print a('abc','def')

b = lambda *z : z

print b(1,23,4.5,'easf')