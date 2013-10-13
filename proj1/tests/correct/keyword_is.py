# Naive uses of the keyword is. Remember 'is' checks identity, not equality

# Simple print
print 10 is 'hello'
print 3 is 5
print 1 is 1

# Using it in if comparisons
if 3 is 3:
    print 'hello'

a = 4
if a is 'what':
    print 'jeesus'

# Using it in a while loop
while 3 is True:
    print 'what'