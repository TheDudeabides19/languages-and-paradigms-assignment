# -------------------------------------------------
# Program 1: Sum and Average of Stock Prices
# -------------------------------------------------

def calculate_sum_and_average(arr, size):
    """Takes an array and its size, returns total sum and average."""
    total = sum(arr)
    average = total / size
    return total, average


# Initialize stock prices
stock = [22.2, 22.7, 23.5, 22.8, 24.3, 25.6]

# Function call
total, average = calculate_sum_and_average(stock, len(stock))

# Display results
print("Program 1: Sum and Average of Stock Prices")
print("Stock Prices:", stock)
print(f"Sum = {total}")
print(f"Average = {average:.2f}")
print("-" * 50)


# -------------------------------------------------
# Program 2: Largest, Second Largest, and Smallest
# -------------------------------------------------

def find_extremes(arr, size):
    """Returns the largest, second largest, and smallest elements."""
    sorted_arr = sorted(arr)
    smallest = sorted_arr[0]
    second_largest = sorted_arr[-2]
    largest = sorted_arr[-1]
    return largest, second_largest, smallest


# Initialize selling prices
selling = [80, 50, 35, 65, 127, 77, 92, 85, 123, 90, 55, 124]

# Function call
largest, second_largest, smallest = find_extremes(selling, len(selling))

# Display results
print("Program 2: Selling Price Analysis")
print("Selling Prices:", selling)
print(f"Largest = {largest}")
print(f"Second Largest = {second_largest}")
print(f"Smallest = {smallest}")
print("-" * 50)


# -------------------------------------------------
# Program 3: Reverse a Specific Row in a Matrix
# -------------------------------------------------

def reverse_row(matrix, rows, cols, row_number):
    """Reverses the elements of a specific row in the matrix."""
    if 0 <= row_number < rows:
        matrix[row_number] = matrix[row_number][::-1]
    else:
        print("Invalid row number.")
    return matrix


# Initialize matrix
quantity = [
    [2, 4, 3, 6, 9],
    [5, 8, 9, 3, 7],
    [1, 4, 3, 2, 10]
]

rows = len(quantity)
cols = len(quantity[0])

# Display original matrix
print("Program 3: Reverse a Row in a Matrix")
print("Original Matrix:")
for r in quantity:
    print(r)

# Reverse row 1 (second row)
reverse_row(quantity, rows, cols, 1)

# Display modified matrix
print("\nMatrix After Reversing Row 1:")
for r in quantity:
    print(r)
print("-" * 50)
