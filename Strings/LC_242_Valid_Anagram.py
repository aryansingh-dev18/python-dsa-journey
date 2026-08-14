"""
Problem: LeetCode 242 - Valid Anagram

Topic:
- Strings
- Hashing
- Frequency Counting
- Dictionary

Approach:
- First, compare the lengths of both strings.
- If lengths are different, they cannot be anagrams.
- Create two dictionaries to store character frequencies.
- Traverse both strings and count the frequency of every character.
- Compare both frequency dictionaries.
- If both dictionaries are equal, the strings are anagrams.

Example:
s = "anagram"
t = "nagaram"

Output:
True

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for ch in s:
            if ch in freq_s:
                freq_s[ch] += 1
            else:
                freq_s[ch] = 1

        for ch in t:
            if ch in freq_t:
                freq_t[ch] += 1
            else:
                freq_t[ch] = 1

        return freq_s == freq_t

obj = Solution()

print(obj.isAnagram("anagram","nagaram"))
