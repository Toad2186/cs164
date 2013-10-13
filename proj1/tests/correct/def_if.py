# Test putting it statements inside a def

# Naive if inside
def hello(a):
    if a == 2:
        return 2

# Def with multiple arguments, and if-else.
def world(a, b):
    if a == b:
        return 3
    else:
        return 10

# Def with three arguments and if, else and elif constructs.
def sir(a, b, c):
    if a == c:
        return 10
    elif b > c:
        return 1
    else:
        return 3

# Call each of them.
hello(2)
world(3, 4)
sir(1, 2, 3)