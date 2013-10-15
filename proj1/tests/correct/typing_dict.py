# Simple dict defining
a::dict of [str,str] = {'hello':'1', 'world':'1'}
b::dict of [str,int] = {'one':1, 'two':2}
c::dict of str,int = {'one':1}

# Dictionary accessing with typed dicts
x::dict of [str, int] = {'a':1, 'b': 2}
print x['a']
print 'b' not in a