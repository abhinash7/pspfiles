# Harmful

def wrap_add_for_console_output(x, y):
print('--------------------------------')
print(str(x + y))
print('--------------------------------')
wrap_add_for_console_output(2,3)


# Idiomatic

def for_console_output(func):
def wrapper(*args, **kwargs):
print('--------------------------------')
print(str(func(*args, **kwargs)))
print('--------------------------------')
return wrapper
@for_console_output
def add(x, y):
return x + y
add(3, 2)
