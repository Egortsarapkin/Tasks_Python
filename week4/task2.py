"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/permutations/submissions
"""


class Solution(object):
    def permute(self, nums):
        def permute1(nums):
            result = []

            def backtrack(current_permutation):

                if len(current_permutation) == len(nums):
                    result.append(current_permutation[:])
                    return

                for num in nums:
                    if num not in current_permutation:
                        current_permutation.append(num)
                        backtrack(current_permutation)
                        current_permutation.pop()

            backtrack([])
            return result

        return permute1(nums)
