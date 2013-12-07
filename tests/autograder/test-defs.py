x = 3

def f1(): return 7

def f2():
  return 8

def f3(): return

def f4(x):
  print x
  if x > 3:
    return x
  else:
    return x+1

def f5(x,y):
  print x + y

print f1()
print f2()
print f3()
print f4(2)
print f4(4)
f5(9, 17)
