"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):

        def l_substring(s):
            char_index_map = {}
            start = 0
            max_length = 0

            for index, char in enumerate(s):
                if char in char_index_map and char_index_map[char] >= start:
                    start = char_index_map[char] + 1
                char_index_map[char] = index
                max_length = max(max_length, index - start + 1)

            return max_length

        return l_substring(s)
