"""
Leetcode: https://leetcode.com/problems/number-of-islands/
Date: 6-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        R = len(grid)
        C = len(grid[0])
        visited = [[0] * C for _ in range(R)]

        def dfs(row, col):
            if row < 0 or row >= R or col < 0 or col >= C or visited[row][col] or grid[row][col] == "0":
                return

            visited[row][col] = 1
            for direction in directions:
                nr, nc = row + direction[0], col + direction[1]
                dfs(nr, nc)
            return

        count = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == "1" and not visited[row][col]:
                    count += 1
                    dfs(row, col)
        return count

def test():
    solution = Solution()
    test_cases = [
        [ [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","1"]], 2 ],
        [ [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1 ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.numIslands(test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()
