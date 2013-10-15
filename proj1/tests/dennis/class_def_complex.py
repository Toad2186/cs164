# Class definition with an instance variable which is a statement
# Also use the keyword 'self' to refer to the object itself.
class A:
    x=1+2
    def hello(self):
        if self.x < 10:
            return self.x

x = A()
y = x.hello()

# Class definition with multiple methods
class Car:
    def on(self):
        return "no gas"
    def park(self):
        return 'You cannot park'
    def parallel_park(self):
        return self.park()

tesla = Car()
a = tesla.on()
b = tesla.park()