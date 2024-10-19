"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/integer-to-roman/submissions/
"""


class Solution(object):
    def intToRoman(self, num):

        def int_to_roman(num):

            val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            syms = [
                "M",
                "CM",
                "D",
                "CD",
                "C",
                "XC",
                "L",
                "XL",
                "X",
                "IX",
                "V",
                "IV",
                "I",
            ]

            roman_numeral = ""

            for i in range(len(val)):

                while num >= val[i]:
                    roman_numeral += syms[i]
                    num -= val[i]

            return roman_numeral

        return int_to_roman(num)
