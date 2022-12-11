"""
Leetcode: https://leetcode.com/problems/delete-greatest-value-in-each-row/
Date: 11-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid:
            row.sort(reverse=True)
        maxSumResult = 0
        for col in range(len(grid[0])):
            maxSumResult += max([grid[row][col] for row in range(len(grid))])
        return maxSumResult

def test():
    testcases = [
        [[[1, 2, 4], [3, 3, 1]], 8],
        [[[1, 2, 4], [2, 3, 1]], 7],
        [[[10]], 10]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.deleteGreatestValue(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)
