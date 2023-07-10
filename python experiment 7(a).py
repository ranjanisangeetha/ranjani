import numpy as np

# Get the elements of the list from the user
elements = input("Enter the elements of the list (space-separated): ").split()

# Convert the list of elements to a one-dimensional NumPy array
arr = np.array(elements)

# Print the original list
print("Original List:", elements)

# Print the one-dimensional NumPy array
print("NumPy Array:", arr)
