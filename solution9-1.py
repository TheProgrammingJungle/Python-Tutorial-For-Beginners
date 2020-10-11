while True:
	print()
	x = input("Enter the first number: ")
	if x == "quit":
		break
	if x == "skip":
		continue

	y = input("Enter the second number: ")
	if y == "quit":
		break
	if y == "skip":
		continue

	op = input("Enter the operation you want to perform: ")
	if op == "quit":
		break
	if op == "skip":
		continue

	x = int(x)
	y = int(y)

	if not y and op == "/":
		print("Division by 0 not allowed")
		continue

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
	else:
		opstring = ""

	print()
	if not opstring:
		print("Invalid operator entered")
	else:
		print(f"{opstring} of {x} and {y} resulted in {result}")
print("Calculator Terminated")
print()