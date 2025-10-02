import sys


def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling for zero division and non-numeric inputs.

    Args:
        numerator: The numerator as string
        denominator: The denominator as string

    Returns:
        str: Result of division or error message
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Try to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


def main():
    if len(sys.argv) != 3:
        print("Usage: python division_calculator.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)


if __name__ == "__main__":
    main()