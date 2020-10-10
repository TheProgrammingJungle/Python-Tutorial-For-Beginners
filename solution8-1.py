print()
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
op = input("Enter the operation you want to perform: ")

opstring = ""
result = 0

if op == '+':
	opstring = "Addition"
	result = x + y
elif op == '-':
	opstring = "Subtraction"
	result = x - y
elif op == '*':
	opstring = "Multiplication"
	result = x * y
elif op == '/':
	opstring = "Division"
	result = x / y

print()
if not opstring:
	print("Invalid operator entered")
else:
	print(f"{opstring} of {x} and {y} resulted in {result}")
print()
