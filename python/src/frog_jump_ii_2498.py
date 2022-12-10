"""
Leetcode: https://leetcode.com/problems/frog-jump-ii/
Date: 10-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        res = stones[1] - stones[0]
        N = len(stones)
        for i in range(2, N, 2):
            res = max(res, stones[i] - stones[i-2])
        for i in range(3, N, 2):
            res = max(res, stones[i] - stones[i-2])
        return res


def test():
    testcases = [
        [[0, 2, 5, 6, 7], 5],
        [[0, 3, 9], 9]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.maxJump(testcase[0])
        assert result == testcase[1], 'Testcase #{} failed! Expected: {}. Got: {}'.format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
