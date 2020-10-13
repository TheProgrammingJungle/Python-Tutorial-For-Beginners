n = int(input("Enter n: "))
m = int(input("Enter m: "))
print()

for i in range(1,n+1):
	for j in range(1,m+1):
		print(f"{i} X {j} = {i*j}")
	print()
