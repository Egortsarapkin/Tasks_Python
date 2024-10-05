"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/4sum/description/
"""


class Solution(object):
    def fourSum(self, nums, target):

        def four_sum(nums, target):
            nums.sort()
            n = len(nums)
            quadruplets = set()

            for i in range(n):
                for j in range(i + 1, n):
                    left, right = j + 1, n - 1
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total < target:
                            left += 1
                        elif total > target:
                            right -= 1
                        else:
                            quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                            left += 1
                            right -= 1

            return list(map(list, quadruplets))

        return four_sum(nums, target)
