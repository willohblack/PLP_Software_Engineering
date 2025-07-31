# List of words
words = ["apple", "banana", "kiwi", "grape", "strawberry", "mango"]

# Use list comprehension to find words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with an odd number of characters:")
print(odd_length_words)
