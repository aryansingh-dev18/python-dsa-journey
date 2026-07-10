"""
Problem: Check if Array is Sorted
Topic: Arrays
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
"""

arr = [1,2,3,4,5]

is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

print(is_sorted)




        

    


