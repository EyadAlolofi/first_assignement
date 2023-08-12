# Example 1: Adding two numbers using a lambda function
add = lambda x, y: x + y
result = add(2, 3)
print(result)

# Example 2: Squaring numbers using a lambda function and map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Example 3: Filtering even numbers using a lambda function and filter()
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)