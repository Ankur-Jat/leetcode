"""
Leetcode: https://leetcode.com/problems/climbing-stairs/
Date: 12-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


def test():
    testcases = [
        [1, 1],
        [2, 2],
        [3, 3],
        [9, 55]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.climbStairs(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
