"""
leetcode.com/problems/array/
url:   https://leetcode.com/problems/rotate-image/submissions/
"""
class Solution(object):
    def rotate(self, matrix):
        def rotate(matrix):
            n = len(matrix)

            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            for i in range(n):
                matrix[i].reverse()
        return rotate(matrix)
