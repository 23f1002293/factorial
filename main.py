import sys

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
