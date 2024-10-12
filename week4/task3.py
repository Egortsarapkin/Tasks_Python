"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/permutations-ii/submissions
"""


class Solution(object):
    def permuteUnique(self, nums):
        def permute_unique(nums):
            nums.sort()
            result = []
            current_permutation = []
            used = [False] * len(nums)

            def backtrack():

                if len(current_permutation) == len(nums):
                    result.append(current_permutation[:])
                    return

                for i in range(len(nums)):

                    if used[i]:
                        continue

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    current_permutation.append(nums[i])
                    backtrack()

                    used[i] = False
                    current_permutation.pop()

            backtrack()
            return result

        return permute_unique(nums)
