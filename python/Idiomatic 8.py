# Harmful

def f(a, L=[]):
L.append(a)
return L
print(f(1))
print(f(2))
print(f(3))
# This will print
#
# [1]
# [1, 2]
# [1, 2, 3]

#Idiomatic

def f(a, L=None):
if L is None:
L = []
L.append(a)
return L
print(f(1))
print(f(2))
print(f(3))
# This will print
# [1]
# [2]
# [3]
