# Overloading except with typed variables

def a():
    print 'hello'

def a(x::int):
    print x

def a(y::str):
    print 'str: ' + y

x = a()
y = a(3)
z = a('hello')