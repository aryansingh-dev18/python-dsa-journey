"""
Problem: LeetCode 56 - Merge Intervals

Topic:
- Arrays
- Sorting
- Intervals

Approach:
- First, sort the intervals according to their starting value.
- Create an empty list 'merged' to store the final intervals.
- Add the first interval to 'merged' by default.
- Traverse the remaining intervals.
- Compare the current interval's start with the end of the last
  interval in 'merged'.
- If current start <= last merged end, the intervals overlap.
  Merge them by taking the maximum of both ending values.
- If there is no overlap, add the current interval separately.

Example:
Input:
[[1,3], [2,6], [8,10], [15,18]]

Output:
[[1,6], [8,10], [15,18]]

Time Complexity:
- O(n log n) because of sorting.

Space Complexity:
- O(n) for storing the merged intervals.
"""

intervals = [[1,3], [2,6], [8,10], [15,18]]

intervals.sort()
merged = []

merged.append(intervals[0])

for current in intervals[1:]:
    
    if current[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], current[1])
        
    else:
        merged.append(current)

print(merged)