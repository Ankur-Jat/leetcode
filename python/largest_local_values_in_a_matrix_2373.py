"""
Leetcode: https://leetcode.com/problems/largest-local-values-in-a-matrix/
Date: 14-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def max_value(i, j):
            directions = [
                [i-1, j-1],
                [i-1, j],
                [i-1, j+1],
                [i, j-1],
                [i, j],
                [i, j+1],
                [i+1, j-1],
                [i+1, j],
                [i+1, j+1]
            ]
            max_value = 0
            for direction in directions:
                max_value = max(max_value, grid[direction[0]][direction[1]])
            return max_value

        N = len(grid)
        new_grid = [[0] * (N - 2) for _ in range(N-2)]
        for i in range(N-2):
            for j in range(N-2):
                new_grid[i][j] = max_value(i+1, j+1)
        return new_grid


def test():
    testcases = [
        [ [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]], [[9,9],[8,6]] ],
        [ [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]], [[2,2,2],[2,2,2],[2,2,2]] ]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.largestLocal(testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
