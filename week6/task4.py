"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/arithmetic-slices/
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        def countArithmeticSubarrays(nums):
            n = len(nums)
            if n < 3:
                return 0

            total_count = 0
            current_length = 0

            for i in range(2, n):

                if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                    current_length += 1
                    total_count += current_length
                else:
                    current_length = 0

            return total_count

        return countArithmeticSubarrays(nums)