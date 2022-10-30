"""
Leetcode: https://leetcode.com/problems/maximum-sum-of-an-hourglass/
Date: 2-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxSumOfHourGlass = 0
        R = len(grid) - 2
        C = len(grid[0]) - 2
        for row in range(R):
            localSumOfHourGlass = grid[row][0] + grid[row][1] + grid[row][2] + grid[row+1][1] + grid[row+2][0] + grid[row+2][1] + grid[row+2][2]
            maxSumOfHourGlass = max(maxSumOfHourGlass, localSumOfHourGlass)
            for col in range(1, C):
                localSumOfHourGlass += grid[row][col+2] - grid[row][col-1] + grid[row+1][col+1] - grid[row+1][col] + grid[row+2][col+2] - grid[row+2][col-1]
                maxSumOfHourGlass = max(maxSumOfHourGlass, localSumOfHourGlass)
        return maxSumOfHourGlass


def test():
    solution = Solution()
    test_cases = [
        [ [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]],  30, ],
        [ [[6,2,1,3],[4,2,1,5],[1,2,8,7],[4,1,2,9]], 28, ],
        [ [[1,2,3],[4,5,6],[7,8,9]], 35, ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.maxSum(test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
