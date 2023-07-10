filename = input("Enter the filename: ")

# Get the number of lines to read from the user
n = int(input("Enter the number of lines to read: "))

# Open the file in read mode
try:
    with open(filename, 'r') as file:
        # Read 'n' lines from the file
        lines = file.readlines()[:n]

        # Print the lines
        for line in lines:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")




















