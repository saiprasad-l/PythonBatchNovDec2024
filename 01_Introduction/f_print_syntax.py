"""
Purpose : print() function syntax and usage

"""

print("name =", name)
print("Name of student is name")


print("Name of student is" + name)
print("Name of student is " + name)
print()

print("Name of Student is ", name)
print("Name of Student is ", name, sep=" ")
print("Name of Student is ", name, sep="-")
print("Name of Student is ", name, sep="")


print(1, 2, 3, 4, 5, 6)
print(1, 2, 3, 4, 5, 6, sep=" ")


print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")


name = 1232
print("Name of Student is", name)

#print('Name of Student is' + name)
#TypeError : 

print("1 + 2                =", 1+2)
print("'1'  +  '2'          =", "1" + "2")
print()

# NOTE: Python is a strictly typed language
print("1 + 2 =", 1 + 2) # addition
print("'1' + '2' =", "1" + "2") # string concatenation
print()

# 1 + '2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# type converters str(), int(), float()
print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")
print()


print("int ('234') =", int("234"))

# print("int('23.4T =", int('23.4')) # ValueError: invalid literal for il
# print("int('two') int('two')) # ValueError: invalid literal for int