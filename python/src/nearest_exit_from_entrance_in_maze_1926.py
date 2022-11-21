"""
Leetcode: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
Date: 21-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        R = len(maze)
        C = len(maze[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            r, c, steps = queue.popleft()
            if [r, c] != entrance and (r == 0 or c == 0 or r == (R-1) or c == (C-1)):
                return steps

            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == '.':
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps+1))
        return -1


def test():
    testcases = [
        [[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2], 1],
        [[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2],
        [[[".", "+"]], [0, 0], -1]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.nearestExit(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase: #{} failed! Expected: {}. Got: {}".format(
            index, testcase[2], result)


if __name__ == "__main__":
    test()
