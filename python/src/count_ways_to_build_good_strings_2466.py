"""
Leetcode: https://leetcode.com/problems/count-ways-to-build-good-strings/
Date: 12-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict


class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        dp = defaultdict(lambda: 0)
        dp[0] = 1
        for i in range(1, high+1):
            dp[i] = (dp[i-zero] + dp[i-one]) % (10**9 + 7)
        result = 0
        for i in range(low, high+1):
            result = (result + dp[i]) % (10**9 + 7)
        return result % (10**9 + 7)


def test():
    testcases = [
        [[3, 3, 1, 1], 8],
        [[3, 3, 2, 2], 0],
        [[2, 3, 1, 2], 5],
        [[200, 200, 10, 1], 764262396]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.countGoodStrings(*testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
