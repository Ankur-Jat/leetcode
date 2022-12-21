"""
Leetcode: https://leetcode.com/problems/possible-bipartition/
Date: 21-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n, dislikes):
        if n <= 1 or len(dislikes) == 0:
            return True
        adjacency_list = defaultdict(list)
        for edge in dislikes:
            adjacency_list[edge[0] - 1].append(edge[1] - 1)
            adjacency_list[edge[1] - 1].append(edge[0] - 1)
        color = [0] * n
        visited = set()
        for vertex in range(n):
            if vertex in visited:
                continue
            color[vertex] = 1
            queue = deque([vertex])
            while queue:
                node = queue.popleft()
                newColor = 2 if color[node] == 1 else 1
                visited.add(node)
                for neighbour in adjacency_list[node]:
                    if neighbour in visited:
                        continue
                    if color[neighbour] and color[neighbour] == color[node]:
                        return False
                    color[neighbour] = newColor
                    queue.append(neighbour)
        return True


def test():
    testcases = [
        [4, [[1, 2], [1, 3], [2, 4]], True],
        [3, [[1, 2], [1, 3], [2, 3]], False],
        [5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.possibleBipartition(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[2], result)


if __name__ == "__main__":
    test()
