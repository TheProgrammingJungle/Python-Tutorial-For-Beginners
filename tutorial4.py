# Python Programming Tutorial for Beginners
# Part-4: Strings and String Formatting

# -----------------------------------------------------------------------------

# String is a datatype to store textual data. They can be enclosed within
# either single quotes('TEXT_HERE') or double quotes("TEXT_HERE").
s = "text"
s = 'text'

# If one wants to use double quotes(") as part of the text, then the text
# should be enclosed within single quotes(') otherwise program will cause a
# syntax error. Similar thing goes when one wants to use single quotes(') as
# part of the text, then the text should be enclosed within double quotes(").

# s = "He quoted - "Life is awesome""   # Throws syntax error
s = 'He quoted - "Life is awesome"'		# Correct usage
print(s)

# s = 'Hey what's up'					# Throws syntax error
s = "Hey what's up"						# Correct usage
print(s)

print()  # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Multiline strings in python can be created by enclosing the multiline text
# within either triple single quotes(''') or triple double quotes(""").
s = """Brace Yourself
This is
The Programming Jungle"""
print(s)

s = '''Programming is a superpower.
You can create awesome stuff with it.'''
print(s)

print()  # To add an extra line in the output.

# -----------------------------------------------------------------------------

# String multiplication: Can multiply a string with an integer(say y) to repeat
# that string y number of times.
s = "*" * 8
print(s)

# String concatenation: Using + operator to join multiple strings together.
first_friend = "Alice"
second_friend = "Bob"
third_friend = "Charlie"

s = "He met " + first_friend + ", " + second_friend + " and " + third_friend
print(s)

print()  # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Exercise 1:-
# Print this pattern(without #) using string concatenation and multiplication.

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# For solution, check the code in solution4-1.py.

# -----------------------------------------------------------------------------

# Problems with string concatenation - Becomes cumbersome with more complex &
# large strings. Solutions - i) String Format method and ii) f-strings.

# String Format method: Can be used to place values inside a string directly at
# places marked with braces.
s = "He met {}, {} and {}".format(first_friend, second_friend, third_friend)
# This will print "He met Alice, Bob and Charlie".
print(s)

# Instead of having empty braces we can also add "indices" inside these braces.
# Indices basically represent the values passed inside the .format method.
# They count from 0 till (number of values passed - 1). In above case valid
# indices as 0(first_friend), 1(second_friend) and 2(third_friend).
# By using indices inside braces at some location, the corresponding value will
# be inserted into the location.

s = "He met {2}, {0} and {1}".format(first_friend, second_friend, third_friend)
# This will print "He met Charlie, Alice and Bob".
print(s)

s = "He met {2}, {2} and {2}".format(first_friend, second_friend, third_friend)
# This will print "He met Charlie, Charlie and Charlie".
print(s)

# This will throw an error as 3 is not a valid index here.
# s = "He met {1}, {2} and {3}".format(first_friend, second_friend, third_friend)

print()  # To add an extra line in the output.

# f-strings: Can be used to directly place expressions inside of the string.
# String has to start with an f before the opening quote. Not just strings or
# string variables, these braces can contain generalized expressions.
# Expressions in python are something that are evaluated first and then their
# values are used. Examples: 2 + 3 * 4, or x + 2, or s.upper(), etc.
# Don't worry if you dont understand expressions now, we will study these in
# further tutorials.

s = f"He met {first_friend}, {second_friend} and {third_friend}"
# This will print "He met Alice, Bob and Charlie".
print(s)

s = f"Sum of 10 and 20 is {10 + 20}"
print(s)
# Observe here you dont need to do any type conversions from int to string.
# This is the power of f-strings, similar expression evaluations works for
# values passed in string format method.
s = "Sum of 10 and 20 is {}".format(10 + 20)
print(s)

# -----------------------------------------------------------------------------

# Exercise 2:-
# Ask someone his name, color, and favorite sport. And print them together.
# See the output(run solution4-2.py) for the required format of asking
# questions and printing final answer.

# For solution, check the code in solution4-2.py.
