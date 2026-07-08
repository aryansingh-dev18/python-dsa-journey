"""
Problem: Linear Search
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
"""

arr = [12, 45, 67, 23, 89]
target = 67

for i in range(len(arr)):
    # compare arr[i] with target
    if arr[i] == target:
        print("Found at index",i)
        break
else:
  print("Not found")