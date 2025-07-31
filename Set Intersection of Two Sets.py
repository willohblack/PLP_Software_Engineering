# Get user input for the first set
set1_input = input("Enter integers for the first set (separated by spaces): ")
set1 = set(map(int, set1_input.split()))

# Get user input for the second set
set2_input = input("Enter integers for the second set (separated by spaces): ")
set2 = set(map(int, set2_input.split()))

# Find the intersection
common_elements = set1.intersection(set2)

print(f"Common elements in both sets: {common_elements}")
