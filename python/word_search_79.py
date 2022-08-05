"""
Leetcode: https://leetcode.com/problems/word-search/
Date: 5-Aug-2022
Author: Ankur Jat
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        R = len(board)
        C = len(board[0])
        visited = [[0] * C for _ in range(R)]

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= R or col < 0 or col >= C or visited[row][col]:
                return False
            if visited[row][col] or board[row][col] != word[index]:
                return False

            visited[row][col] = 1
            for direction in directions:
                nr, nc = row + direction[0], col + direction[1]
                if dfs(nr, nc, index+1):
                    return True
            visited[row][col] = 0
            return False

        for row in range(R):
            for col in range(C):
                if dfs(row, col, 0):
                    return True
        return False

def test():
    solution = Solution()
    test_cases = [
        [ [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCEG", False ],
        [ [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCE", True ],
        [ [["a"]], "a", True ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.exist(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()
