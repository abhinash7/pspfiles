# Harmful

def print_list(list_value, sep):
print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list, ' ')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')


#Idiomatic

def print_list(list_value, sep=' '):
print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')
