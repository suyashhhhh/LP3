# Practical -1 : Write a program to calculate Fibonacci numbers and find its step count
# Both recursive and non-recursive

def recursive_fibonacci(n): #defining a recursive function
	if n <= 1:
		return n
	else:
		return recursive_fibonacci(n-1) + recursive_fibonacci(n-2) #will return sum of two terms

def non_recursive_fibonacci(n):
	first = 0
	second = 1
	step_count = 2
	print(first)
	print(second)
	while step_count < n:
		third = first + second
		first = second
		second = third
		print(third)
		step_count += 1
	return step_count

n = int(input("Enter the nth term: "))
print("The fibonacci sequence using recursive function:")
for i in range(n):
	print(recursive_fibonacci(i))

print("The fibonacci sequence using non-recursive function")
steps = non_recursive_fibonacci(n)
print(f"Steps: {steps}")