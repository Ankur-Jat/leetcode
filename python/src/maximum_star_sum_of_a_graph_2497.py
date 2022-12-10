"""
Leetcode: https://leetcode.com/problems/maximum-star-sum-of-a-graph/
Date: 10-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict

class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return max(vals)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = []
        for i, v in enumerate(vals):
            starSum = []
            for u in graph[i]:
                if vals[u] > 0:
                    starSum.append(vals[u])
            starSum.sort(reverse=True)
            result.append(vals[i] + sum(starSum[:k]))
        return max(result)


def test():
    testcases = [
        [[1, 2, 3, 4, 10, -10, -20], [[0, 1], [1, 2],
                                      [1, 3], [3, 4], [3, 5], [3, 6]], 2, 16],
        [[-5], [], 0, -5]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.maxStarSum(testcase[0], testcase[1], testcase[2])
        assert result == testcase[3], 'Testcase #{} failed! Expected: {}. Got: {}'.format(
            index, testcase[3], result)


if __name__ == "__main__":
    test()
