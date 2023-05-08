# This function creates a square grid and fills it with numbers based on the specified corner, size and maximum number.
def square_grid():
    # Read input from the user
    size = int(input("Enter the size of the square grid (between 1 and 8): "))
    corner = input("Enter the corner to start from (TL, TR, BL, BR): ").upper()
    maximum_number = int(input("Enter grid maximum number: "))

    # Create a 2D list (grid) filled with zeros
    grid = [[0] * size for i in range(size)]

    # Based on the specified corner, fill the grid with numbers in the appropriate order
    if corner == "TL":  # Start from top-left corner
        for i in range(size):
            number = 1 + i  # The first number in each row increases by 1
            for j in range(size):
                if number > maximum_number:  # If the number exceeds the maximum number, fill the cell with 0
                    grid[i][j] = 0
                else:  # Otherwise, fill the cell with the number
                    grid[i][j] = number
                number += 1  # Increment the number for the next cell in the row
    elif corner == "TR":  # Start from top-right corner
        for i in range(size):
            number = size + i  # The first number in each row is equal to the size plus the row number
            for j in range(size):
                if number > maximum_number:  # If the number exceeds the maximum number, fill the cell with 0
                    grid[i][j] = 0
                else:  # Otherwise, fill the cell with the number
                    grid[i][j] = number
                number -= 1  # Decrement the number for the next cell in the row
    elif corner == "BL":  # Start from bottom-left corner
        for i in range(size):
            number = size - i  # The first number in each row is equal to the size minus the row number
            for j in range(size):
                if number > maximum_number:  # If the number exceeds the maximum number, fill the cell with 0
                    grid[i][j] = 0
                else:  # Otherwise, fill the cell with the number
                    grid[i][j] = number
                number += 1  # Increment the number for the next cell in the row
    elif corner == "BR":  # Start from bottom-right corner
        for i in range(size):
            number = maximum_number - i  # The first number in each row is equal to the maximum number minus the row number
            for j in range(size):
                if number > 0:  # If the number is positive, fill the cell with the number
                    grid[i][j] = number
                else:  # Otherwise, fill the cell with 0
                    grid[i][j] = 0
                number -= 1  # Decrement the number for the next cell in the row

    # Print the grid row by row, separated by spaces
    for row in grid:
        print(' '.join(str(e) for e in row))
