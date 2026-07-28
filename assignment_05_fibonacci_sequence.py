# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def generate_fibonacci_terms(count):
    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def is_fibonacci_number(number):
    if number < 0:
        return False

    first, second = 0, 1
    while first < number:
        first, second = second, first + second

    return first == number


def main():
    terms = int(input("How many terms? "))
    if terms <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci_terms(terms)
    print("Fibonacci sequence:", end=" ")
    for value in sequence:
        print(value, end=" ")
    print()

    number = int(input("Enter a number to check: "))
    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

