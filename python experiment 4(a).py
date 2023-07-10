def tuple_to_string(tuple_value):
    # Join the elements of the tuple using a comma and convert it to a string
    string_value = ', '.join(map(str, tuple_value))
    return string_value

# Get user input for the number of elements
num_elements = int(input("Enter the number of elements in the tuple: "))

# Get user input for the values of the elements
elements = []
for i in range(num_elements):
    value = input("Enter the value of element {}: ".format(i + 1))
    elements.append(value)

# Convert the list to a tuple
tuple_value = tuple(elements)

# Call the function to convert the tuple to a string
result = tuple_to_string(tuple_value)

# Print the result
print("Tuple:", tuple_value)
print("String:", result)
