"""
Leetcode: https://leetcode.com/problems/evaluate-division/
Date: 9-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict, deque
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1.0 / value
        
        def value_of_path(path):
            value = 1.0
            while len(path) > 1:
                first = path[0]
                second = path[1]
                value = value * graph[first][second]
                path = path[1:]
            return value

        result = []
        for query in queries:
            if query[0] == query[1] and len(graph[query[0]].keys()) > 0:
                result.append(1.0)
            elif graph[query[0]].get(query[1], None) != None:
                result.append(graph[query[0]][query[1]])
            else:
                stack = deque()
                path = [query[0]]
                stack.append([query[0], path])
                found = False
                visited = {}
                while stack:
                    node, inner_path = stack.pop()
                    if node in visited:
                        continue
                    visited[node] = True
                    if node != query[0] and node == query[1]:
                        found = True
                        path = inner_path
                        break
                    for key in graph[node].keys():
                        if key not in visited:
                            stack.append([key, inner_path + [key]])
                if not found:
                    result.append(-1.0)
                else:
                    value = value_of_path(path)
                    result.append(value)
                    graph[query[0]][query[1]] = value
                    graph[query[1]][query[0]] = 1.0 / value
        return result


def test():
    solution = Solution()
    test_cases = [
        [ [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],  [6.00000,0.50000,-1.00000,1.00000,-1.00000]],
        [ [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]], [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000] ],
    ]

    for index, test_case in enumerate(test_cases):
        assert solution.calcEquation(test_case[0], test_case[1], test_case[2]) == test_case[3], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
