"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/
"""

import math


class Solution(object):

    def longestPalindrome(self, s):
        def expanda(st, left, right):
            while left >= 0 and right < len(st) and st[left] == st[right]:
                left -= 1
                right += 1

            return right - left - 1

        end = 0
        start = 0
        for i in range(0, len(s)):
            len1 = expanda(s, i, i)
            len2 = expanda(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = math.ceil(i - (length - 1) / 2)
                end = math.floor(i + length / 2)

        return s[int(start): (int(end + 1))]
