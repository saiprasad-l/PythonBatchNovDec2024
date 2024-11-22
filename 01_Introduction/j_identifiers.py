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




# Identifiers - User-defined variables

#       Naming Convention
#           1. keywords should not be used as identifiers
#           2. first character: a-z, A-Z,
#           3. remaining chars: a-z, A-Z, _, 0-9
# -----     Rule 1
# True = 123 # SyntaxError: cannot assign to True
# None = 'Nothing' # SyntaxError: cannot assign to True


true = 123
none = "Nothing"

true_value = 123
none_result = "Nothing"

# ---- Rule 2 & 3
name = "Priyanka"
name_of_student = "Priyanka"
first_name = "priyanka"
student_1 = "Priyanka"
class_02_a = "Python comment operations"
first___child = "Satvik"

PI = 3.1416
DOZEN = 12


# $name = "Priyanka"
# name-of-student = "Priyanka"
# name_of_student = "Priyanka"
# 1st_name = "Priyanka"

_2nd_student = "someone"

_job = "software development"
__role = "Product support"
___salary = 1231231232312323233



# OOP -> name mangling
# variable  -> Public variable
# _variable -> Protected variable
# variable -> Private variable

