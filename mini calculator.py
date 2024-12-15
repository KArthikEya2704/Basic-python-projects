
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Welcome to the Mini Calculator")
    print("Select operation:")
    print("+. Add")
    print("-. Subtract")
    print("*. Multiply")
    print("/. Divide")

    while True:
        try:
            choice = input("Enter the number of the operation you'd like to perform (+ - * / or 'q' to quit): ")

            if choice.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in ['+', '-', '*', '/']:
                print("Invalid input. Please select a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '+':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '-':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '*':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '/':
                print(f"The result is: {divide(num1, num2)}")

        except ValueError:
            print("Error: Please enter a valid number.")
if __name__ == "__main__":
    calculator()
