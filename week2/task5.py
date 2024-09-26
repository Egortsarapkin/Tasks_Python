"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-break/
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        def word_break(s, wordDict):
            word_set = set(wordDict)
            n = len(s)
            dp = [False] * (n + 1)

            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break

            return dp[n]

        return word_break(s, wordDict)
