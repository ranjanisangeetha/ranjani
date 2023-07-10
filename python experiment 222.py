def can_obtain_string(first_string, second_string):
    first_string = list(first_string)  # Convert the first string to a list for easy removal
    for char in second_string:
        if char in first_string:
            first_string.remove(char)
        else:
            return "NO"
    if not first_string:
        return "YES"
    else:
        return "NO"

# Prompt the user for input
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

result = can_obtain_string(first_string, second_string)
print(result)

