# Simple overloading check

def hello():
    print 'hello'

def hello(a,b):
    print a, b

def hello(a,b,c):
    print a,b,c

hello()
hello(1,2)
hello('a','b','c')
