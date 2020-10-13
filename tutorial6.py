# Python Programming Tutorial for Beginners
# Part-6: Integers, Float, and Arithmetic Operations

# -----------------------------------------------------------------------------

# Examples of Integers
x = 34
y = 0
z = -1

# Examples of Floating Point numbers
x = -1.034
y = 0.12
# If nothing mentioned after decimal point, 0 is assumed.
z = 2. 	# Same as z = 2.0

# -----------------------------------------------------------------------------

x = 10
y = 5

print(x+y)	# 15
print(x-y)	# -5
print(x*y)	# 50

x = 11
print(x/y)	# 2.2 (float division)
print(x//y)	# 2 (integer division - quotient)
print(x%y)	# 1 (remainder operation) 

x = 2
print(x**y) # 32 = 2*2*2*2*2 (Exponentiation)

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Operator Precedence - Governs the order of evaluation.
# Brackets(( )) > Exponentiation(**) > Mult/Div/Rem (*,/,//,%) > Add/Sub (+,-)
# For operators having same precedence, evaluation happens from left to right.

print(2 + 4 + 5 * 3)	# 21
print(11//5*10)			# 20
print(11*10//5)			# 22

print(11*11//5)			# 24
print(11*(11//5))		# 22

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# round function is used to round off floating point numbers.
x = 1.23
print(round(x))		# 1
print(round(x,1))	# 1.2
print(round(x,2))	# 1.23

# abs function is used convert negative numbers to their positive counterparts.
print(abs(-5))		# 5
print(abs(5))		# 5

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Augmented Assignment Operator: x op= y (applicable for all 7 arithmetic ops)

x = 5
x += 5		# same as x = x + 5
print(x)	# 10

x *= 5		# same as x = x * 5
print(x)	# 50

y = 2
y **= 3		# same as y = y ** 3 => 2*2*2
print(y)	# 8

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Exercise 1:- 
# Predict the output.

x = 1
y = -1
print(x + y)     	# 0
print(abs(y))    	# 1
z = x + abs(y)
print(z)		 	# 2
z += x
print(z)		 	# 3
print(z % (x + 1)) 	# 1
w = (z + x) * (z + y) + 2 
print(w)			# 10
print(w/z)			# 3.3333333
print(w//z)			# 3
print(w//3*w)		# 30
print(w*w//3)   	# 33
