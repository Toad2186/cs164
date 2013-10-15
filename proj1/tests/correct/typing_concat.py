# Test concatenation when using typed strs
x::str = 'hello'
y::str = 'goodbye'
z = x + y

# Test one typed and one untyped
a = 'he said'
b::str = 'stuff'
c = a + b