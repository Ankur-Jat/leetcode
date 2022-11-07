"""
Leetcode: https://leetcode.com/problems/maximum-69-number/
Date: 7-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = [digit for digit in str(num)]
        for index, digit in enumerate(result):
            if digit == '6':
                result[index] = '9'
                break
        return int(''.join(result))


def test():
    testcases = [
        [9669, 9969],
        [69, 99],
        [99, 99]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.maximum69Number(testcase[0])
        assert result == testcase[1], "Testcase #{} failed. Expected: {}, got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
