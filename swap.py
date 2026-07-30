# swap.py

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display before swapping
print("\nBefore Swapping:")
print("First Number =", a)
print("Second Number =", b)

# Swap the values
a, b = b, a

# Display after swapping
print("\nAfter Swapping:")
print("First Number =", a)
print("Second Number =", b)