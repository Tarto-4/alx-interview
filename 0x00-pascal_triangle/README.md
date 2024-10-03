# Pascal's Triangle

## Task: Pascal's Triangle

This project implements Pascal’s Triangle, a triangular array of binomial coefficients. Each number in Pascal's Triangle is the sum of the two numbers directly above it in the previous row.

### Problem Statement

Write a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of size `n`.

- If `n <= 0`, return an empty list.
- You can assume that `n` will always be an integer.

### Example

For `n = 5`, calling `pascal_triangle(5)` should return:

```python
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]

Usage

    Clone this repository:

    bash

git clone https://github.com/tarto-4/alx-interview.git

Navigate to the 0x00-pascal_triangle directory:

bash

cd alx-interview/0x00-pascal_triangle

Run the script:

bash

./0-main.py

Example Output:

bash

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]

File Structure

    0-pascal_triangle.py: Contains the pascal_triangle(n) function that generates Pascal's Triangle.
    0-main.py: Script to test the pascal_triangle function by printing the output for n = 5.

Code Explanation

The function pascal_triangle(n) constructs Pascal’s Triangle row by row:

    Each row starts and ends with 1.
    The middle elements are the sum of the two numbers directly above them in the previous row.
    The function loops n times to generate the triangle.