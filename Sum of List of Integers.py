# Ask the user to enter numbers separated by spaces
user_input = input("Enter integers separated by spaces: ")

# Convert the input into a list of integers
numbers = list(map(int, user_input.split()))

# Compute the sum
total = sum(numbers)

print(f"The sum of the list is: {total}")
