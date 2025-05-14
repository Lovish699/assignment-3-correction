def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print(" Factorial is not defined for negative numbers.")
        else:
            print(f"✅ The factorial of {num} is {factorial(num)}")
    except ValueError:
        print(" Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()