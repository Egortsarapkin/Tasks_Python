"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution(object):
    def characterReplacement(self, s, k):

        def characterReplacement(s, k):
            left, max_count, max_length = 0, 0, 0
            count = [0] * 26

            for right in range(len(s)):

                count[ord(s[right]) - ord('A')] += 1
                max_count = max(max_count, count[ord(s[right]) - ord('A')])


                while (right - left + 1) - max_count > k:
                    count[ord(s[left]) - ord('A')] -= 1
                    left += 1


                max_length = max(max_length, right - left + 1)

            return max_length
        return characterReplacement(s, k)