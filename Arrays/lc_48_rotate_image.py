"""
Problem: LeetCode 48 - Rotate Image

Topic:
- Arrays
- Matrix
- In-place Manipulation
- Transpose

Approach:
- Rotate the square matrix 90 degrees clockwise.
- First transpose the matrix by swapping:
    matrix[i][j] with matrix[j][i]
- Then reverse every row.
- Transpose + reversing each row gives a 90-degree clockwise rotation.
- The matrix is modified in-place, so no extra matrix is required.

Example:
Input:
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Output:
[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

Time Complexity:
- O(n²)

Space Complexity:
- O(1)
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(n):
    matrix[i].reverse()

print(matrix)