try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition of two numbers: {a + b}")
    print(f"Subtraction of two numbers: {a - b}")

except ValueError:
    print("Please enter valid numbers.")

