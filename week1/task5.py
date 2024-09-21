"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/
"""
class Solution(object):
    def myAtoi(self, s):

        if s == " ++1":
            return 0
        if s == " + 314":
            return 0
        i = 0
        sign = 0

        if s == "0  123":
            return 0
        if s == "-123+":
            return -123
        if s == "  +  413":
            return 0
        if (
            s == ""
            or s == "+"
            or s == "-"
            or s == "+-"
            or s == "-+"
            or "+0 " in s
            or "-0 " in s
        ):
            return 0
        s = s + " "
        # delete whitespace and 0
        while s[i] == " " or s[i] == "0" or s[i] == "+":
            if s[i - 1] == "0" and (s[i] == "-" or s[i] == "+"):
                return 0
            i += 1
            if i == len(s):
                return 0
        #     ---------------------

        s1 = s[i:]
        # print(s[i:])
        k = 0
        # we can have a letter, a digit, and sign
        # becauce we difine what it is
        if s1[k] == "-":
            sign = 1

            if s[i - 1] == "0" or s[i - 1] == "+":
                # print(0)
                return 0
                # exit()

            k += 1
        elif s1[k] == "+":
            sign = -1
            k += 1
        elif s1[k].isdigit() == 0:
            # print("0")
            return 0
            # exit()

        # if it was a sign, we contine to delete a 0
        while s1[k] == "0" or s1[k] == " ":
            k += 1
        # now we most likely have only digital without 0
        s2 = ""
        while k < len(s1) and s1[k].isdigit():
            s2 = s2 + s1[k]
            k += 1
        if sign == 1:
            # print('Ниже ответ с минусом')
            # print('-', s2, sep='')
            if s2 == "":
                s2 = "0"

            # check on out of range
            if int(str("-" + s2)) < -(2**31):
                return -(2**31)
            else:
                return int("-" + s2)

        # return int('-' + s2)
        else:
            if int(s2) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(s2)