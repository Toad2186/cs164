# Testing a class where the attributes use multiple assignment

class a:
    a = 10
    (b,c,d) = (15,12,9)
    def hello(self, x, y):
        a = 5
        print a

# This should wipe out the class definition interestingly enough.
a = 15
