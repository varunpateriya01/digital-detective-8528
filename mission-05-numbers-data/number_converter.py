"""Convert a non-negative decimal integer to binary and hexadecimal."""

value = int(input("Enter a non-negative decimal integer: "))
if value < 0:
    raise ValueError("Please enter a non-negative integer.")
print("Binary:", format(value, "b"))
print("Hexadecimal:", format(value, "X"))
