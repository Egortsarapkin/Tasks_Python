"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        def minSubArrayLen(target, nums):
            left = 0
            current_sum = 0
            min_length = float("inf")

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum >= target:
                    min_length = min(min_length, right - left + 1)
                    current_sum -= nums[left]
                    left += 1

            return min_length if min_length != float("inf") else 0

        return minSubArrayLen(target, nums)
