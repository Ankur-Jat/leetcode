"""
Leetcode: https://leetcode.com/problems/integer-to-roman/
Date: 20-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        if num >= 1000:
            result = "M" * (num // 1000)
            num %= 1000
        if num >= 900:
            result += "CM"
            num -= 900
        if num >= 500:
            result += "D"
            num -= 500
        if num >= 400:
            result += "CD"
            num -= 400
        if num >= 100:
            result += "C" * (num // 100)
            num %= 100
        if num >= 90:
            result += "XC"
            num -= 90
        if num >= 50:
            result += "L"
            num -= 50
        if num >= 40:
            result += "XL"
            num -= 40
        if num >= 10:
            result += "X" * (num // 10)
            num %= 10
        if num >= 9:
            result += "IX"
            num -= 9
        if num >= 5:
            result += "V"
            num -= 5
        if num >= 4:
            result += "IV"
            num -= 4
        if num >= 1:
            result += "I" * num
        return result


def test():
    solution = Solution()
    testcases = [
        [2345, "MMCCCXLV"],
        [2, 'II'],
        [99, 'XCIX']
    ]
    for index, testcase in enumerate(testcases):
        assert solution.intToRoman(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
