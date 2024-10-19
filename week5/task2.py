"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams/
"""
class Solution(object):
    def groupAnagrams(self, strs):
        def groupAnagrams(strs):
            anagrams = {}

            for s in strs:

                key = ''.join(sorted(s))

                if key not in anagrams:
                    anagrams[key] = []
                anagrams[key].append(s)

            return list(anagrams.values())

        return groupAnagrams(strs)