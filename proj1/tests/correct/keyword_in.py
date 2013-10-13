# In already appears in a lot of the other tests. This is just a sanity check

b = [1,2,3]

# Naive use.
print 3 in b

# Using in a for statement
if 3 in b:
    print 'hello'

# Using in a loop
for a in b:
    print a