"""
Leetcode: https://leetcode.com/problems/perfect-squares/
Date: 22-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            j = 1
            dp.append(float('inf'))
            while (i - j*j) >= 0:
                dp[i] = min(
                    dp[i],
                    dp[i - j*j] + 1
                )
                j += 1
        return dp[-1]


def test():
    testcases = [
        [3, 3],
        [4, 1],
        [12, 3],
        [13, 2],
        [2876, 4],
        [10000, 1]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.numSquares(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
