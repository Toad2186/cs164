# Simple tests for while
while False:
    print "hello"

x = False
while x or False:
    print "world"
    x = True

while 1 > 4:
    print "what"

while (3 < 2):
    print 'lol'

i = 5
while i < 10:
    i = i + 1

a = [1,2,3,4,5]
while 10 in a:
    print 'thirty'
