"""
Problem: LeetCode 54 - Spiral Matrix

Topic:
- Arrays
- Matrix
- Boundary Traversal

Approach:
- Use four boundaries to keep track of the unprocessed matrix:
    top, bottom, left, right
- Traverse the matrix in four directions:
    1. Top row: left → right
    2. Right column: top → bottom
    3. Bottom row: right → left
    4. Left column: bottom → top
- After processing each boundary, move it inward.
- Use boundary checks before traversing the bottom row and left
  column to avoid duplicate elements in edge cases.
- Store every visited element in the answer list.

Example:
Input:
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Output:
[1,2,3,6,9,8,7,4,5]

Time Complexity:
- O(m × n)

Space Complexity:
- O(m × n) for the output list.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ans = []

top = 0
bottom = len(matrix) - 1

left = 0
right = len(matrix[0]) - 1

while top <= bottom and left <= right:

    for i in range(left,right + 1):
        ans.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        ans.append(matrix[i][right])
    right  -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1

print(ans)