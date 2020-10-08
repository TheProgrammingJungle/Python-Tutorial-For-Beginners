# Python Programming Tutorial for Beginners
# Part-5: String Methods

# -----------------------------------------------------------------------------

s = "the PRogRamming JunGle"

# len is a general purpose function that gives(returns) the length of several
# objects in python like string, list, tuple, etc.
print(len(s)) # Prints 22 (Count the characters to verify, include spaces also)

# String methods - can be used to manipulate/modify string objects.
# String are 'Immutable' in Python, hence methods do not modify the original
# string, but rather return a new string after applying the method. 

# .upper() method makes each letter of the string uppercase.
print(s.upper()) # Prints -> "THE PROGRAMMING JUNGLE"

# .lower() method makes each letter of the string lowercase.
print(s.lower()) # Prints -> "the programming jungle"

# .title() method makes the first letter of each word uppercase, and all the
# remaining letters in the word lowercase.
print(s.title()) # Prints -> "The Programming Jungle"

# Since string is immutable, 's' is still the same.
print(s) # Prints -> "the PRogRamming JunGle"

# To change 's', we can reassign it to the string returned after the
# application of the method. Here s.upper() returns(gives) an uppercase version
# of string in 's', now we reassign 's' variable to store/refer the new string.
s = s.upper() 
print(s) # Prints -> "THE PROGRAMMING JUNGLE"

# .strip() method removes whitespace from left and right of the string.
s = "   the PRogRamming JunGle   "
print(s)
print(s.strip()) # Prints -> "the PRogRamming JunGle"

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Indexing in Python (0-based)
# Indices start from 0 and go upto length of the object - 1.
s = "jungle"
print(s[0]) 	# Prints -> 'j'
print(s[3]) 	# Prints -> 'g'
print(s[5]) 	# Prints -> 'e'

# This will throw an index out of range error as only valid indices are from
# 0 to len(s)-1 = 5. Hence 6 is not valid index for this string.
# print(s[6])

# Negative indexing in Python
# In the opposite direction indices go from -1 to -length of object.
# Here it goes from -1 to -len(s) = -6. -1 denotes the rightmost character, and
# -6 denotes the leftmost character in the string.
print(s[-1]) 	# Prints -> 'e'
print(s[-3]) 	# Prints -> 'g'
print(s[-6]) 	# Prints -> 'j'

# This will throw an index out of range error as -7 is out of valid range.
# print(s[-7])

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

s = "i am a hero"

# .find(pattern) method allow us to find the index of the first occurence of
# pattern string in the main string on which the method is applied.
print(s.find("am"))		# Prints 2
print(s.find("hero"))	# Prints 7
# Although there are two occurences of 'a' in the above string, only index
# corresponding to the first occurence is returned.
print(s.find("a"))		# Prints 2
# find method returns -1 if the string to be searched is absent in main string.
print(s.find("b"))		# Prints -1

# .replace(old_pattern, new_pattern) method help us to change all occurences of
# old_pattern in main string to the new_pattern specified.
print(s.replace("am", "wanna be")) # Prints -> "i wanna be a hero"

# Remember strings are immutable hence 's' is still the same.
print(s) # Prints -> "i am a hero"

# To actually change 's', just reassign.
s = s.replace("a","aaaaa")
print(s) # Prints -> "i aaaaam aaaaa hero"

# .count(pattern) method allow us to find number of occurences of pattern
# string in the main string.
print(s.count("a"))		# Prints 10
print(s.count("hero"))	# Prints 1
print(s.count("zero"))	# Prints 0

# If we just want to find if a pattern is part of the string and do not care
# about its index, we can use 'in' operator. It returns a boolean - True or
# False depending on if pattern string is part of main string or not.
print("hero" in s)	# Prints True
print("zero" in s)	# Prints False

print() # To add an extra line in the output.

# -----------------------------------------------------------------------------

# Exercise 1:- 
# Predict the output.

s = "ProGraMming exErCise"
s.upper() 					# s remains same
print(s) 					# Prints -> "ProGraMming exErCise"
s.lower() 					# s becomes = "ProGraMming exErCise"
print(s[0]) 				# Prints -> "P"
print(s.title()) 			# Prints -> "Programming Exercise"
s = s.upper() 				# s becomes = "PROGRAMMING EXERCISE"
print(s) 					# Prints -> "PROGRAMMING EXERCISE"
print(s[2]) 				# Prints -> "O"
print(s[-2]) 				# Prints -> "S"
s.replace('R', 'ROR') 		# s becomes = "PROGRAMMING EXERCISE"
print(s) 					# Prints -> "PROGRAMMING EXERCISE"
s = s.replace('R', 'ROR') 	# s becomes = "PROROGRORAMMING EXERORCISE"
print(s) 					# Prints -> "PROROGRORAMMING EXERORCISE"
print(s.find('ROR')) 		# Prints -> 1
print("ROGROR" in s) 		# Prints -> True
print("ABC" in s) 			# Prints -> False
print(s.count('OR')) 		# Prints -> 3
len(s) 						# Nothing gets printed.
