# Factorial Calculator

## Summary

This is a minimal, working application that provides two ways to calculate the factorial of a given non-negative integer:
1. A command-line Python script (`main.py`).
2. An interactive web interface (`index.html`).

The factorial of a non-negative integer `n`, denoted by `n!`, is the product of all positive integers less than or equal to `n`. For example, `5! = 5 * 4 * 3 * 2 * 1 = 120`. The factorial of 0 is defined as 1.

## Setup

### Prerequisites
- Python 3.x installed on your system.
- A modern web browser to use the interactive version.

### Installation
No external libraries are required. Simply download the files to a local directory.

## Usage

### Command-Line Script
To use the Python script, run it from your terminal and pass a non-negative integer as a command-line argument.

```bash
# Syntax
python main.py <number>

# Example
python main.py 5
```

Expected output:
```
The factorial of 5 is 120
```

### Web Interface
Open the `index.html` file in your web browser. Enter a non-negative integer into the input field and click "Calculate". The result will be displayed on the page.

## Code Explanation

### `main.py`
This script calculates the factorial of a number provided via the command line.
- It imports the `sys` module to access command-line arguments.
- The `factorial(n)` function computes the factorial iteratively. It includes error handling to ensure the input is a non-negative integer.
- The main execution block (`if __name__ == "__main__":`) parses the command-line argument, calls the `factorial` function, and prints the result. It also handles potential `ValueError` (if the input is not a valid integer) and argument count errors.

### `index.html`
This file provides a user-friendly web interface for the factorial calculator.
- **HTML**: Sets up a simple form with a number input field and a submit button. A paragraph element is designated to display the result.
- **JavaScript**:
  - An event listener is attached to the form's `submit` event.
  - When the form is submitted, the script prevents the default page reload.
  - It reads the number from the input field.
  - A JavaScript function calculates the factorial using `BigInt` to handle large numbers without losing precision.
  - The result is then rendered into the designated paragraph element on the page. Input validation is performed to handle negative numbers or empty input.

## License

This project is licensed under the MIT License.
