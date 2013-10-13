# Test all the basic typing declarations.

a::int = 3
b::$myint = 3
c::list of [int] = [3]
d::list of int = [3]
e::dict of [str, list of int] = {'one': [1]}


# TODO: Typing with function-type denotation
#           f::(int, int) -> int =