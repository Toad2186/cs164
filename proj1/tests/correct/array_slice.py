# Test simple list slicing
a = [1,2,3,4]
b = a[:]
c = a[0:]
d = a[1:2]
e = a[:3]

# Negative list slicing. Should this work in our spec?
d = a[-2:]
