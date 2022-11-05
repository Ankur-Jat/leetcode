"""
Leetcode: https://leetcode.com/problems/word-search-ii/
Date: 5-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def get_node(self, char, node):
        return node.children.get(char, None)

    def delete_word(self, word):
        node = self.trie
        path = []
        for char in word:
            path.append(node)
            node = node.children[char]
        for index in range(len(word) - 1, -1, -1):
            char = word[index]
            node = path[index]
            if node.children[char].children.keys():
                node.children[char].is_word = False
                return
            else:
                del node.children[char]


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.board = board

        self.R = len(self.board)
        self.C = len(self.board[0])
        self.result = []
        for row in range(self.R):
            for col in range(self.C):
                char = board[row][col]
                if char in self.trie.trie.children:
                    visited = [[False] * self.C for _ in range(self.R)]
                    self.find_word(row, col, visited, '', self.trie.get_node(
                        self.board[row][col], self.trie.trie))
        return self.result

    def find_word(self, r, c, visited, word, node):
        visited[r][c] = True
        word += self.board[r][c]
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        if node.is_word:
            self.result.append(word)
            self.trie.delete_word(word)

        for direction in directions:
            nr, nc = r + direction[0], c + direction[1]
            if nr >= 0 and nr < self.R and nc >= 0 and nc < self.C and not visited[nr][nc] and self.trie.get_node(self.board[nr][nc], node):
                self.find_word(nr, nc, visited, word,
                               self.trie.get_node(self.board[nr][nc], node))

        # word = word[:-1]
        visited[r][c] = False


def test():
    testcases = [
        [[["o", "a", "a", "n"], ["t", "t", "a", "e"], ["i", "h", "k", "r"], [
            "i", "f", "l", "v"]], ["oath", "pea", "eat", "rain", "oat", "ot"], ["oat", "oath", "ot", "eat"]],
        [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], [
            "i", "f", "l", "v"]], ["oath", "pea", "eat", "rain", "hklf", "hf"], ["oath", "eat", "hklf", "hf"]]
    ]

    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.findWords(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase #{} failed. Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
