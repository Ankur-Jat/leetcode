"""
Leetcode: https://leetcode.com/problems/where-will-the-ball-fall/
Date: 1-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        R = len(grid)
        C = len(grid[0])

        def get_next_cell(row, col):
            nc = col + grid[row][col]
            if row >= R or row < 0 or col >= C or col < 0 or nc >= C or nc < 0:
                return -1, -1, -1
            if grid[row][col] == grid[row][nc]:
                prev_col = col
                if grid[row][col] == 1:
                    row, col = row + 1, col + 1
                else:
                    row, col = row + 1, col - 1
                if row >= R:
                    return -1, -1, col
                return row, col, None
            else:
                return -1, -1, -1

        result = []
        counter = 0
        for ball in range(len(grid[0])):
            row, col = 0, ball
            while True:
                row, col, outcome = get_next_cell(row, col)
                if outcome != None:
                    result.append(outcome)
                    break
        return result


def test():
    testcases = [
        [[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
          [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]], [1, -1, -1, -1, -1]],
        [[[-1]], [-1]],
        [[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]], [0, 1, 2, 3, 4, -1]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.findBall(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
