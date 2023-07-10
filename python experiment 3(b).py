def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

# Prompt the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Prompt the user to enter the list values
num_list = []
for i in range(num_elements):
    value = int(input("Enter value for index {}: ".format(i)))
    num_list.append(value)

if is_ascending(num_list):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
