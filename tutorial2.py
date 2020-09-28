# Python Programming Tutorial for Beginners
# Part-2: Variables and Data Types

# ---------------------------------------------------------------------------------------

# Initialization or Declaration of variable x
x = 5 
print(x)
x = 6
print(x)
x = 10
print(x)
print() # To add an extra line in the output.

# Output will be: 
# 5
# 6
# 10
# This shows that python code is interpreted line-by-line sequentially.


# print(y)
# y = 10
# This will give an 'error' as y variable is accessed before its declaration.

# ---------------------------------------------------------------------------------------

# Naming convention for variables:
# Variable names can contain: numbers(0-9), letters(a-zA-Z), and underscores(_).
# Variable names cannot start with a number.

# ---------------------------------------------------------------------------------------

# Exercise 1 :-
# Select variable names which are valid.

A = 1
b_ = 2
_abc = 3
# Not a valid variable name as it starts with a number 7.
# 7abs = 4
Z87_ = 5
# Not a valid variable name as it contains $ and @ symbols.
# A$a@b = 6
_ = 7
aB8 = 8
# Not a valid variable name as it starts with a number 8.
# 8a = 9

print(A)
print(b_)
print(_abc)
print(Z87_)
print(_)
print(aB8)
print() # To add an extra line in the output.

# ---------------------------------------------------------------------------------------

# Four basic datatypes :-
# 1) integers: -1, 0, 1000 (int)
# 2) decimal/floating point numbers: -3.45, 0.01, 1.760 (float)
# 3) strings: "hi", 'helloworld' (str)
# 4) boolean: True, False (bool)

# Python is case-sensitive language
# True is not same as true
# x not same as X

x = 2
y = 1.77
z = "try"
w = True
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print() # To add an extra line in the output.

# ---------------------------------------------------------------------------------------

# Exercise 2 :-
# What is the datatype for these variables.

a = True
b = 0
# When nothing is written after decimal point, it is assumed to be 0, hence c = 2.0 here.
c = 2.0
d = "Hello"
e = 'False'
f = -1.5
g = 10000000000
# Here false is not a correct boolean value, as python is case sensitive.
# h = false

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
