
"""
Leetcode: https://leetcode.com/problems/reachable-nodes-with-restrictions/
Date: 8-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict, deque
class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        def build_adj_list():
            adj_list = defaultdict(dict)
            for edge in edges:
                adj_list[edge[0]][edge[1]] = True
                adj_list[edge[1]][edge[0]] = True
            return adj_list

        restricted_dict = {}
        for key in restricted:
            restricted_dict[key] = True
        adj_list = build_adj_list()
        count = 0
        visited = {}
        stack = deque()
        stack.append(0)
        while stack:
            node = stack.pop()
            if node in visited or node in restricted_dict:
                continue
            count += 1
            visited[node] = True
            for vertices in adj_list[node].keys():
                if vertices not in visited and vertices not in restricted_dict:
                    stack.append(vertices)
        return count

def test():
    solution = Solution()
    test_cases = [
        [ 7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5], 4 ],
        [ 7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4, 2, 1], 3]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.reachableNodes(test_case[0], test_case[1], test_case[2]) == test_case[3], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()
