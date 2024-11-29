"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""


class Solution(object):
    def longestSubstring(self, s, k):

        def longestSubstring(s, k):
            if len(s) == 0:
                return 0


            char_count = {}
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1


            for char in char_count:
                if char_count[char] < k:

                    return max(longestSubstring(substring, k) for substring in s.split(char))


            return len(s)
        return longestSubstring(s, k)