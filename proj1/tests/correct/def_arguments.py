# Try writing def with multiple arguments passed in

def hilfiger(goodbye):
    print goodbye

def hello(x,y):
    print x, y

# Multiple arguments, returning different sized tuples
def a(x,y,z):
    return (x,y,)

def b(x,y,z):
    return (x,y,z)

def c(x,y,z):
    return (x)

d = hilfiger('woah')
e = hello('dear','sir')
f = a(1,2,3)
f = b(3, "hello", True)
