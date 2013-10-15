# More complicated defs with typing

# List typed def
def goodbye(x::list of int):
    if 10 in x:
        return 10
    else:
        return 0

# Dictionary typed def
def hello(x::dict of [str, int]):
    if 'a' not in x:
        return x['a']
    else:
        return 'what'

