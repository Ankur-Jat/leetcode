"""
Leetcode: https://leetcode.com/problems/count-nodes-with-the-highest-score/
Date: 10-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Tree(object):
    def __init__(self, val):
        self.leftNodes = 0
        self.rightNodes = 0
        self.left = None
        self.right = None
        self.val = val


class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        def buildTree():
            treeNodes = [Tree(val) for val in range(N)]
            for index, parent in enumerate(parents[1:]):
                if not treeNodes[parent].left:
                    treeNodes[parent].left = treeNodes[index+1]
                else:
                    treeNodes[parent].right = treeNodes[index+1]
            return treeNodes[0]

        def updateChildNodesSize(node):
            if not node:
                return 0
            node.leftNodes = updateChildNodesSize(node.left)
            node.rightNodes = updateChildNodesSize(node.right)
            return node.leftNodes + node.rightNodes + 1

        def calculateMaxScoreNode(node):
            if not node:
                return
            # NodesInParent * nodesInLeft * nodesInRight
            score = max(N - node.leftNodes - node.rightNodes - 1, 1) * \
                max(node.leftNodes, 1) * max(node.rightNodes, 1)
            if score > self.maxScore:
                self.maxScore = score
                self.maxScoreNodesCount = 1
            elif score == self.maxScore:
                self.maxScoreNodesCount += 1
            calculateMaxScoreNode(node.left)
            calculateMaxScoreNode(node.right)

        N = len(parents)
        root = buildTree()
        updateChildNodesSize(root)
        self.maxScore = float('-inf')
        self.maxScoreNodesCount = 0
        calculateMaxScoreNode(root)
        return self.maxScoreNodesCount


def test():
    testcases = [
        [[-1, 2, 0, 2, 0], 3],
        [[-1, 2, 0], 2],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.countHighestScoreNodes(testcase[0])
        assert result == testcase[1], "Testcase: #{} failed. Expeccted: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
