# Python Programming Tutorial for Beginners
# Part-7: Comparison and Logical operators

# -----------------------------------------------------------------------------

# Comparison Operators:
# Greater Than (>), Greater Than or Equal to (>=)
# Less Than (<), Less Than or Equal to (<=)
# Equal to (==), Not Equal to (!=)
# Comparing two items returns a boolean value (True/False)

print(2 < 3) # True
print(2 > 3) # False
print(3 >= 3) # True

print(4 == 5) # False
print(4 == 4) # True
print(4 != 4) # False
print(4 != 5) # True

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# These operators also work for string, which are compared lexicographically,
# i.e. in dictionary order. Word that comes later in dictionary order is bigger
# (comparison wise) than a word that comes earlier in dictionary.
print('a' < 'c')			# True
print('a' >= 'c')			# False

print('abc' < 'acb')		# True
print('abc' == 'abc')		# True
print('abc' != 'acb')		# True
print('python' < 'java')	# False as python comes later than java.

# Note: if uppercase letters are also present then ordering is based on ASCII
# values, basically all uppercase letters are smaller than lowercase letters.
print('A' < 'a')	  	# True
print('Code' < 'app')	# True

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Difference Between = and == :
# = is assignment operator, we assign some value to a variable using this.
# It does not return any value. 
# print(x = 4)	# This line gives error
#
# == is the equality operator, and it returns True if both left and right sides
# of operator are equal, else False.
x = 4
print(x == 4) # Prints True
print(x == 5) # Prints False

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Logical Operators:
# and, or, not
# and, or : Usage -> x or/and y
# not : Usage -> not x

# and - Both x and y should be True to make result True.
# or - Either x or y (or both) should be True to make result True.
# not -> If x is True, (not x) is False. If x is False, then (not x) is True.

print(True and True)	# True	
print(False and True)	# False
print(False and False)	# False

print(True or True)		# True
print(True or False)	# True
print(False or False)	# False

print(not True)			# False
print(not False)		# True

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Operator precedence after including comparison and logical operators
# (in decreasing order - top to bottom):
# ()
# **
# *,/,//,%
# +,-
# >, <, >=, <=, ==, !=
# not
# and
# or
#
# Note: For operators on same level, execution happens from left to right.

print(2>3 or 4<5)	# True or False => True
print(2>3 and 4<5)	# True and False => False
print(not 2!=2)		# not False => True
