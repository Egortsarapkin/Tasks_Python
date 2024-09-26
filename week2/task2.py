"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/
"""


class Solution(object):
    def multiply(self, num1, num2):

        def stoint(n):

            num1 = list(n)
            num = 0
            for i in range(0, len(num1)):
                print(num1[len(num1) - 1 - i], 10**i)
                for digit in range(10):
                    if str(digit) == num1[len(num1) - 1 - i]:
                        num += digit * 10**i
            return num

        return str(stoint(num1) * stoint(num2))
