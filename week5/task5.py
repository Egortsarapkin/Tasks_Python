"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution(object):
    def longestConsecutive(self, nums):
        def longest_consecutive(nums):

            num_set = set(nums)
            longest_streak = 0

            for num in nums:

                if num - 1 not in num_set:
                    current_num = num
                    current_streak = 1

                    while current_num + 1 in num_set:
                        current_num += 1
                        current_streak += 1

                    longest_streak = max(longest_streak, current_streak)

            return longest_streak

        return longest_consecutive(nums)
