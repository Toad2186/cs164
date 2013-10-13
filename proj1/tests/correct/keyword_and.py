# Regular python and.
a = 1
b = 2
c = a and b

# Note: This should return b(2) btw.
print c

# Using and in if statements.
d = 4
e = 5
if a and b:
    print "hello world"

if b and e and e:
    print "goodbye world"