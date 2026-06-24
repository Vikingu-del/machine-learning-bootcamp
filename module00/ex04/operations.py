import sys


def operate(a: int, b: int) -> None:
    """This function diplays the sum, diff, prod, quotient and remainder
    of two integers."""
    print(f"Sum:         {a + b}")
    print(f"Difference:  {a - b}")
    print(f"Product:     {a * b}")
    if b != 0:
        print(f"Quotient:    {a / b}")
        print(f"Remainder:   {a % b}")
    else:
        print("ERROR (division by zero)")
        print("ERROR (modulo by zero)")


def main():
    if len(sys.argv) != 3:
        print("Usage: python operations.py <number1> <number2>")
        sys.exit(1)
    try:
        operate(int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)


if __name__ == "__main__":
    main()
