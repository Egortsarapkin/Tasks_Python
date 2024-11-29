"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/repeated-dna-sequences/submissions/
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        def findRepeatedDnaSequences(s):
            seen = set()
            duplicates = set()

            for i in range(len(s) - 9):
                substring = s[i:i + 10]
                if substring in seen:
                    duplicates.add(substring)
                else:
                    seen.add(substring)

            return list(duplicates)

        return findRepeatedDnaSequences(s)