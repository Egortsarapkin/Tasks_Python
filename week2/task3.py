"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/
"""


class Solution(object):
    def groupAnagrams(self, strs):

        def group_anagrams(strs):
            anagrams = {}

            for s in strs:

                key = "".join(sorted(s))
                if key not in anagrams:
                    anagrams[key] = []
                anagrams[key].append(s)

            return list(anagrams.values())

        return group_anagrams(strs)
