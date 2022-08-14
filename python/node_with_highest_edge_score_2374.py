"""
Leetcode: https://leetcode.com/problems/node-with-highest-edge-score/
Date: 14-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        edge_score = {}
        for from_node, to_node in enumerate(edges):
            edge_score[to_node] = edge_score.get(to_node, 0) + from_node
        max_node = None
        max_node_value = None
        for node, node_score in edge_score.items():
            if max_node == None:
                max_node = node
                max_node_value = node_score
            elif (node_score > max_node_value) or (node_score == max_node_value and node < max_node):
                max_node = node
                max_node_value = node_score
        return max_node


def test():
    testcases = [
        [ [1,0,0,0,0,7,7,5], 7 ],
        [ [2,0,0,2], 0 ]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.edgeScore(testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
