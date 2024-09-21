"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/
"""
class Solution(object):
    def intToRoman(self, num):

        def int_to_roman(num):
            roman_numerals = [
                (1000, "M"),
                (900, "CM"),
                (500, "D"),
                (400, "CD"),
                (100, "C"),
                (90, "XC"),
                (50, "L"),
                (40, "XL"),
                (10, "X"),
                (9, "IX"),
                (5, "V"),
                (4, "IV"),
                (1, "I"),
            ]
            result = ""
            for value, numeral in roman_numerals:
                while num >= value:
                    result += numeral
                    num -= value
            return result

        return int_to_roman(num)