# Testing nested def statements. Already testing this 'type' of thing with
# closure.py, but more doesn't hurt

def a(x):
    def b(y):
        return y + 3
    return b(x)

x = a(1)
