"""
leetcode.com/problems/array/
url: https://leetcode.com/problems/jump-game-ii
"""

class Solution(object):
    def jump(self, nums):
        def jump1(nums):
            n = len(nums)
            if n <= 1:
                return 0

            jumps = 0
            current_end = 0
            farthest = 0

            for i in range(n - 1):
                farthest = max(farthest, i + nums[i])
                if i == current_end:
                    jumps += 1
                    current_end = farthest
                    if current_end >= n - 1:
                        break

            return jumps
        return jump1(nums)

