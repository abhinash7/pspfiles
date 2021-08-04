# Harmful

def print_addition_table():
for x in range(1, 3):
for y in range(1, 3):
print(str(x + y) + '\n')
def print_subtraction_table():
for x in range(1, 3):
for y in range(1, 3):
print(str(x - y) + '\n')
def print_multiplication_table():
for x in range(1, 3):
for y in range(1, 3):
print(str(x * y) + '\n')
def print_division_table():
for x in range(1, 3):
for y in range(1, 3):
print(str(x / y) + '\n')
print_addition_table()
print_subtraction_table()
print_multiplication_table()
print_division_table()


# Idiomatic

import operator as op
def print_table(operator):
for x in range(1, 3):
for y in range(1, 3):
print(str(operator(x, y)) + '\n')f
f
o
r
o
p
e
r
a
t
o
r
i
n
(
o
p
.
a
d
d
,
o
p
.
s
u
b
,
o
p
.
m
u
l
,
o
p
.
i
t
r
u
e
d
i
v
)
:
   p
r
i
n
t
_
t
a
b
l
e
(
o
p
e
r
a
t
o
r
) 
