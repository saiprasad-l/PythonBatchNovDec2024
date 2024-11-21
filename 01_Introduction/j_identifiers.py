"""
Purpose : Identifiers in Python

    Variable
        1. keyword      -->
        2. Identifier   -->


"""

import keyword

print(keyword.kwlist)


print()

print (True) # True
# print(true) NameError: name 'true' is not defined.

my_value = "something"
print(my_value) # Identifier

# True = "something"
# SyntaxError: cannot assign to True

print(keyword.iskeyword("True"))   #True
print(keyword.iskeyword ("true"))  #False
print(keyword.iskeyword("my_value")) #False

