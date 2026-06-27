"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""
n = int(input("Number of Line: "))
# TODO: Use the function once
def line_generator(n):
    for x in range(n):
        print(f"Line {x + 1}")

line_generator(n)

