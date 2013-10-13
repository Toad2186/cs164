# Testing nested def statements. Already testing this 'type' of thing with
# closure.py, but more doesn't hurt

b = 0

def a():
    def b():
        return b + 3
    return b()

x = a()