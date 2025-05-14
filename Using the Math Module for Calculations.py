import math
try:
    number = float(input("Enter a positive number: "))
    if number <= 0:
        print("Please enter a number greater than 0 for accurate logarithm and square root calculations.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)
        print(f"Square root of {number}: {square_root}")
        print(f"Natural logarithm (log base e) of {number}: {natural_log}")
        print(f"Sine of {number} (in radians): {sine_value}")
except ValueError:
    print("Invalid input. Please enter a valid number.")