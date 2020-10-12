# Python Programming Tutorial for Beginners
# Part-8: If-Elif-Else conditionals

# Example that demonstrates use of if, elif, else statements.
# This also demonstrates nested conditionals.
level = int(input("How much drink remaining: "))

if level >= 90:
	if level == 100:
		print("It's a new bottle")
	else:
		print("Bottle is almost full")
elif level >= 50:
	print("It is still more than half")
elif level >= 25:
	print("It is less than half, but more than a quarter")
else:
	print("Need to buy another drink")

print("Logic complete")

# -----------------------------------------------------------------------------

# Exercise 1 :-
# 
# Make a simple calculator that takes 2 numbers and an op(+, -, * or /) as
# input, and returns the answer. See the output(run solution8-1.py) for the
# required format of input statements and answers,

# For solution, check the code in solution8-1.py.
