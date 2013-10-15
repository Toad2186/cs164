# Simple closure

def a():
    def b():
        return 'hello'
    return b

j = a()
k = j()

# More complicated closure
def plus_2(num):
    def y():
        return num + 2
    return y

x = plus_2(3)
y = x()
