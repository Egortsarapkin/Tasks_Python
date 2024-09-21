"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/
"""
class Solution(object):
    def generateParenthesis(self, n):
        def generate_parentheses(n):
            def backtrack(s="", left=0, right=0):
                if len(s) == 2 * n:
                    result.append(s)
                    return
                if left < n:
                    backtrack(s + "(", left + 1, right)
                if right < left:
                    backtrack(s + ")", left, right + 1)

            result = []
            backtrack()
            return result

        combinations = generate_parentheses(n)
        return combinations
