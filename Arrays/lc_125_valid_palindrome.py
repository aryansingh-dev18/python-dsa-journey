"""
Problem: LeetCode 125 - Valid Palindrome

Topic:
- Two Pointers

Difficulty:
- Easy

Approach:
- Use two pointers, one from the beginning and one from the end.
- Ignore all non-alphanumeric characters.
- Compare characters in lowercase.
- If both characters match, move both pointers.
- If they do not match, return False.
- If all comparisons succeed, return True.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 04/08/2026
"""

s = "rac ecr"

left = 0
right = len(s)-1



while left < right:


    if not s[left].isalnum():
         left += 1
         continue

    elif not s[right].isalnum():
        right -= 1
        continue

    elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
                 
    else:
        print(False)
        break

else:
    print(True)

    
    

