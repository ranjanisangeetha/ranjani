dictionary = {}

# Get the number of key-value pairs from the user
num_pairs = int(input("Enter the number of key-value pairs: "))

# Get the key-value pairs from the user and add them to the dictionary
for i in range(num_pairs):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

# Iterate over the dictionary and print the key-value pairs
for key, value in dictionary.items():
    print(key,value)
