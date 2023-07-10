import numpy as np

# Get the elements of the list from the user
l=list(map(float,input("type number with space:").split()))

print("original list:",l)

#

# Convert the list to a one-dimensional NumPy array
a=np.array(l)

# Print the one-dimensional NumPy array
print("One-dimensional NumPy Array:", a)
