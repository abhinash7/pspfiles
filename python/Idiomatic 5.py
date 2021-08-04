# Harmful

my_container = ['Larry', 'Moe', 'Curly']
index = 0
for element in my_container:
print('{} {}'.format(index, element))
index += 1





#Idiomatic


my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
print('{} {}'.format(index, element))
