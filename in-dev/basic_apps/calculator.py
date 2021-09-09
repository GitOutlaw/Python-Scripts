# Calculator
from replit import clear  # Import clear function
from calculator_art import logo  # Import logo from calculator_art.py


def add(n1, n2):  # Add
    return n1 + n2


def subtract(n1, n2):  # Subtract
    return n1 - n2


def multiply(n1, n2):  # Multiply
    return n1 * n2


def divide(n1, n2):  # Divide
    return n1 / n2


def exponent(n1, n2):  # Exponent
    return n1 ** n2


# Operation symbols dictionary Keys are symbols and Values are function names.=
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,

}


def calculator():
    """Recursion Function: Asks user to input first number, operation and second number.  If 'y' selected,
    continue to add numbers and operations. If 'n' selected, program restarts and allows new input of
    numbers and operations.
    """
    print(logo)

    while True:
        try:
            num1 = float(input("What's the first number?: "))
            break

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            pass

    # Display operation symbols
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Continue or restart calculator
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calcultation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
