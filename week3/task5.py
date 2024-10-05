"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/combination-sum-ii/submissions/
"""


class Solution(object):
    def combinationSum2(self, candidates, target):

        def combinationSum22(candidates, target):
            def backtrack(start, path, target):
                if target == 0:
                    res.append(path)
                    return
                if target < 0:
                    return

                for i in range(start, len(candidates)):

                    if i > start and candidates[i] == candidates[i - 1]:
                        continue

                    if candidates[i] > target:
                        break

                    backtrack(i + 1, path + [candidates[i]], target - candidates[i])

            candidates.sort()
            res = []
            backtrack(0, [], target)
            return res

        return combinationSum22(candidates, target)
