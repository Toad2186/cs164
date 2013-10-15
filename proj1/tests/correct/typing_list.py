# Simple list defining
a::list of [str] = ['hello']
b::list of str = ['hello', 'goodbye']
c::list of [int] = [3, 2]
d::list of int = [3]


# Testing list accessing when we use typing
x::list of [str] = ["a", "b", "c"]
print x[0]
x[0] = "this"
print x[0]
