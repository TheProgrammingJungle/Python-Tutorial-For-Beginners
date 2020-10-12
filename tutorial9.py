# Python Programming Tutorial for Beginners
# Part-9: While loop, break and continue

# -----------------------------------------------------------------------------

# Syntax of while loop:
# while condition:
#	do something
#
# Observe that code after while command is shifted to right(indented). This is
# important, as only the indented part is inside the loop.

# Simple example - as long as i is smaller than 5, we remain in loop.
i = 0
while i < 5:
	print(i)
	i += 1
print("Out of loop")

# Infinite Loop. Uncomment the following 2 lines to try it. You can use
# Control+C to terminate that infinite looping program.
# while True:
# 	print("Looping forever")

# -----------------------------------------------------------------------------

# 'break' statement helps in breaking out of loop when some condition is
# satisfied. In this case, we break if square of some number exceed 1000.
i = 1
while True:
	if i*i > 1000:
		break
	print(i*i)
	i += 1
print("Out of loop")

# -----------------------------------------------------------------------------

# 'continue' statements help in skipping all the instructions in loop present
# below it, and directly jumps to next iteration(run) of the loop.
# In this example we do not greet a person if name contains 'a', we directly
# skip to asking next person's name instead.
while True:
	name = input("name: ")
	if 'a' in name:
		continue
	print("Hi " + name)

# -----------------------------------------------------------------------------

# Exercise 1 :-
#
# Use the simple calculator that we made in part-8 and make it run forever.
# Stop it if user writes "quit" at any point, and restart if person writes
# "skip" at any point. See the output(run solution9-1.py) for the required
# format of input statements, answers, and quit, skip behaviour.

# For solution, check the code in solution9-1.py.
