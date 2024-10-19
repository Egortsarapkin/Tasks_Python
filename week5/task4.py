"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution(object):
    def letterCombinations(self, digits):

        arr = ["", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def deleted_space(n):
            a = list(n)
            while " " in a:
                a.remove(" ")
            new_str = ""
            for i in a:
                new_str = new_str + i
            return new_str

        selected = []
        if digits == "":
            return selected

        for i in digits:
            selected.append(arr[int(i)])

        while len(selected) < 4:
            selected.append(" ")

        otv_arr = []

        for i in selected[0]:
            for j in selected[1]:
                for k in selected[2]:
                    for l1 in selected[3]:
                        s = i + j + k + l1
                        otv_arr.append(s)

        for i in range(len(otv_arr)):
            otv_arr[i] = deleted_space(otv_arr[i])

        return otv_arr