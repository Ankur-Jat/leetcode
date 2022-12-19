"""
Leetcode: https://leetcode.com/problems/find-if-path-exists-in-graph/
Date: 19-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # There are two ways
        # 1. Union-Find
        # 2. Traversing (BFS/DFS)
        # In this approach I'm going with DFS
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        added = set()
        stack = [source]
        added.add(source)
        while stack:
            vertex = stack.pop()
            if vertex == destination:
                return True
            for connectedVertex in graph[vertex]:
                if connectedVertex not in added:
                    stack.append(connectedVertex)
                    added.add(connectedVertex)
        return False


def test():
    testcases = [
        [3, [[0, 1], [1, 2], [2, 0]], 0, 2, True],
        [6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.validPath(testcase[0], testcase[1], testcase[2], testcase[3])
        assert result == testcase[4], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[4], result)


if __name__ == "__main__":
    test()
