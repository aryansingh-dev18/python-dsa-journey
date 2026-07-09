"""
Problem: Second Largest Element
Topic: Arrays
Time Complexity: o(n)
Space Complexity: o(1)
Date: 09-07-2026
"""

arr = [12,65,45,89,23]

largest = arr[0]
second_largest = arr[0]

"""
Problem: Second Largest Element
Topic: Arrays
Time Complexity: O(n)
Space Complexity: O(1)
Date: 09-07-2026
"""

arr = [12, 67, 45, 89, 23]

largest = arr[0]
second = -1

for i in range(1, len(arr)):

    if arr[i] > largest:
        second = largest
        largest = arr[i]

    elif arr[i] > second:
        second = arr[i]

print("Largest:", largest)
print("Second Largest:", second)

