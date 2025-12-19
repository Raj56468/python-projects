#calculator


def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."

try:
    num1_input = float(input("Enter the first number: "))
    num2_input = float(input("Enter the second number: "))
    operation_input = input("Enter the operation (+, -, *, /): ")

    result = calculator(num1_input, num2_input, operation_input)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter numeric values for the numbers.")