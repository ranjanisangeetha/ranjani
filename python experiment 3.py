def find_number_occurrence(numbers, target):
    positive_indices = []
    negative_indices = []
    occurrence = 0

    for i, num in enumerate(numbers):
        if num == target:
            positive_indices.append(i)
            negative_indices.append(i - len(numbers))
            occurrence += 1

    return positive_indices, negative_indices, occurrence


def main():
    n = int(input("Enter the number of elements in the list: "))

    numbers = []
    for i in range(n):
        number = int(input("Enter element #{}: ".format(i + 1)))
        numbers.append(number)

    target = int(input("Enter the number to search for: "))

    positive_indices, negative_indices, occurrence = find_number_occurrence(numbers, target)

    print("Positive Indices:", positive_indices)
    print("Negative Indices:", negative_indices)
    print("Number of occurrences:", occurrence)


if __name__ == "__main__":
    main()
