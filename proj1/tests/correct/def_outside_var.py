# Use a num that is assigned outside the function call
a = 10
def hello():
    b = a
    return b

x = hello()
a = 15
y = hello()
