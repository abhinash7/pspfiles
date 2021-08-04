# Harmful

hash_value = 0
character_hash = {
'a': 97,
'b': 98,
'c': 99,
# ...
'y': 121,
'z': 122,
}
for e in some_string:
hash_value += character_hash[e]
return hash_value

# Idiomatic

hash_value = 0
for e in some_string:
hash_value += ord(e)
return hash_value
