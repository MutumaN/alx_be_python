size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer loop: controls rows
while row < size:
    # Inner loop: controls columns
    for col in range(size):
        print("*", end="")  # Print star without newline
    print()  # Move to the next row after inner loop
    row += 1