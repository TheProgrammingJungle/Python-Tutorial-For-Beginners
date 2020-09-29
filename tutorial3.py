# Python Programming Tutorial for Beginners
# Part-3: Input functions and Type conversions

# We can use input function to take input from a user.
# The user input gets stored in this variable x.
x = input("Enter your favourite color: ")

# String Concatenation - Use '+' operator to join mulitple strings.
print("Your favourite color is " + x + ", Enjoy " + x)

# ----------------------------------------------------------------------------------------------------------

# Exercise 1 :-
# You have 200 one-dollar notes and Andy took some dollars from them.
# You have write a program to ask Andy how many dollars he took.
# And then print how many dollars you still have.

# Solution :-

dollars_taken = input("How many dollars he took: ")

# This print statement will throw an error as "input" function always gives(or returns) a string,
# and int and str operands are not compatible for subtraction. 
# print("I am left with " + (200 - dollars_taken) + " dollars")

# This print statement will throw a different error, that int and string are not compatible for 
# concatenation, as now the middle operand is an int, whereas other two are strings. 
# print("I am left with " + (200 - int(dollars_taken) + " dollars")

# This print will work fine, as first dollars_taken is converted to int, so (200 - int(dollars_taken)) is 
# still an int. Post that we convert it to string, which can now be concatenated with other strings.
print("I am left with " + str(200 - int(dollars_taken)) + " dollars")

# ----------------------------------------------------------------------------------------------------------

# int, float, str, bool -> type conversion functions for respective data types.
# int("i") -> Throw an error, as values passed to this function should be compatible.
# int("34") -> Works fine.

# Special scenario for bool:
# i) Any non-zero number is converted to True, and any zero number(0, 0.0, etc) is converted to False.
# ii) Any non-empty string is converted to True, and any empty string ("", '') is converted to False.

# ----------------------------------------------------------------------------------------------------------

# Exercise 2 :-
# Predict which of the following lines of code will throw an error.
# For the correct ones, write the predicted converted value.

# This will throw an error, as "two" is a string and does not correspond directly to int format.
# a = int("two")
b = int(4.5) 	# 4
c = int("1029") # 1029
d = int(False)  # 0
e = int(4)      # 4

f = float("2.4") # 2.4
g = float(4)     # 4.0
h = float(True)  # 1.0
i = float(2.34)  # 2.34

j = str("hello") # 'hello'
k = str(4000)    # '4000'
l = str(78.948)  # '78.948'
m = str(True)    # 'True'
# Here false is not a string, nor a boolean value(True, False, case sensitive). Hence false is not known. 
# n = str(false)

o = bool("True")  # True
p = bool("")      # False
q = bool(1)       # True
r = bool(0.0)     # False
# Here string is 'False', but still boolean value will be True as this is non empty string.
s = bool("False") # True

# We can print several variables separated by ','.
# To print them in differnt line each, pass a specific argument sep='\n', '\n' denotes newline character.
print(b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,sep='\n')
