# Typing simple definition
def incr(n::int):
    return n + 1

def exclamation (x::str):
    return x + '!'

# Typing where we specify the return type as int
def decr(n::int)::int:
    return n - 1

incr(3)
exclamation('hello')
decr(3)
