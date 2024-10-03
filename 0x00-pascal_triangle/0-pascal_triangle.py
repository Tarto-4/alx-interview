def pascal_triangle(n):
    """ Returns a list of lists representing Pascal's triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Create the new row with 1s at the beginning and end
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
