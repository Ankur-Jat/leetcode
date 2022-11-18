"""
Leetcode: https://leetcode.com/problems/ugly-number/
Date: 18-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        def divide(num, divider):
            while num % divider == 0:
                num /= divider
            return num

        for divider in [5, 3, 2]:
            n = divide(n, divider)
        return n == 1


def test():
    testcases = [
        [6, True],
        [1, True],
        [0, False],
        [-2, False],
        [30, True],
        [60, True],
        [61, False]
    ]

    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.isUgly(testcase[0])
        assert result == testcase[1], "Testcae #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
