# CALCULATOR PROGRAM

def calculator():
    print("\n==== SIMPLE CALCULATOR ====")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation: +, -, *, /, %, ** (power)")
    op = input("Enter operation: ")

    if op == '+':
        print(f"Result = {num1 + num2}")
    elif op == '-':
        print(f"Result = {num1 - num2}")
    elif op == '*':
        print(f"Result = {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("❌ Error: Division by zero not allowed.")
        else:
            print(f"Result = {num1 / num2}")
    elif op == '%':
        print(f"Result = {num1 % num2}")
    elif op == '':
        print(f"Result = {num1 ** num2}")
    else:
        print("❌ Invalid operation symbol.")

calculator()