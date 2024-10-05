"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/combination-sum/
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        def combination_sum(candidates, target):
            result = []

            def backtrack(remaining, combo, start):
                if remaining == 0:
                    result.append(list(combo))
                    return
                elif remaining < 0:
                    return

                for i in range(start, len(candidates)):

                    combo.append(candidates[i])

                    backtrack(remaining - candidates[i], combo, i)

                    combo.pop()

            backtrack(target, [], 0)
            return result

        return combination_sum(candidates, target)
