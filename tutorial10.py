# Python Programming Tutorial for Beginners
# Part-10: For Loops and Nested Loops

# -----------------------------------------------------------------------------

# Simple for loop example, iterating over sequence generated by range function.
for i in range(5): # [0-4]
	print(i, end = " ")
print("out of loop")

# -----------------------------------------------------------------------------

# Range function parameters:
# start - first number of sequence. default 0
# stop - marks end of seq. never part of sequence.
# step - increment between each successive values. default 1

# Variations of range function:
# range(stop) -> 0 to stop-1, with increments of 1.
# range(start, stop) -> start to stop-1, with increments of 1.
# range(start, stop, step) -> start to stop-1, but with increments of step.
# It is possible that stop-1 is not the part of the sequence for 3rd variation.

# Prints 0 1 2 3 4 5 6 7 8 9.
for i in range(10):
	print(i, end=" ")
print()

# Prints 3 4 5 6 7 8 9.
for i in range(3,10):
	print(i, end=" ")
print()

# Prints 3 7.
for i in range(3,10,4):
	print(i, end=" ")
print()

# Prints 3 6 9.
for i in range(3,10,3):
	print(i, end=" ")
print()

# Prints 2 4 6 8.
for i in range(2,10,2):
	print(i, end=" ")
print()

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Iterating in negative direction:
# Start value should be greater than stop value, and step should be negative.

# Prints 10 9 8 7 6 5 4 3 2.
for i in range(10,1,-1):
	print(i,end=" ")
print()

# Prints 10 7 4.
for i in range(10,1,-3):
	print(i,end=" ")
print()

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Nested loops.
for i in range(5):
	for j in range(4):
		print(f"i={i} j={j}")
	print()
print()

# Break statement in for loop.
for i in range(1,100):
	sq = i*i
	if sq > 1000:
		break
	print(sq, end=" ")
print()

# -----------------------------------------------------------------------------

# Exercise 1 :- 
#
# Take two positive integers from the user (n,m). Then generate multiplication
# tables for numbers 1 to n, with each table showing m multiples. See output
# (run solution10-1.py) to get better idea.

# For solution, check the code in solution10-1.py.
