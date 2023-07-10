def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def get_factorial_digits(n):
    fact = factorial(n)
    return len(str(fact))

number = int(input("Enter an integer: "))

if number % 2 == 1:  # Odd number
    fact = factorial(number)
    digits = get_factorial_digits(number)
    print(f"The factorial of {number} is {fact}.")
    print(f"The number of digits in the factorial is {digits}.")
else:  # Even number
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
 








