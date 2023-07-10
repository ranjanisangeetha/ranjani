file1_name = input("Enter the name of File 1: ")
file2_name = input("Enter the name of File 2: ")

# Read the content from File 2
try:
    with open(file2_name, 'r') as file2:
        content = file2.read()

        # Append the content to File 1
        with open(file1_name, 'a') as file1:
            file1.write(content)

    print("Content from", file2_name, "has been added to", file1_name)

except FileNotFoundError:
    print("File not found.")
