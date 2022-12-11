"""
Leetcode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Date: 11-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursiveMaxPathSum(node):
            if not node:
                return 0
            leftSum = max(recursiveMaxPathSum(node.left), 0)
            rightSum = max(recursiveMaxPathSum(node.right), 0)
            self.maxSum = max(
                self.maxSum,
                leftSum + rightSum + node.val
            )
            return max(
                node.val + leftSum,
                node.val + rightSum
            )
        self.maxSum = float('-inf')
        recursiveMaxPathSum(root)
        return self.maxSum


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(2)
    assert solution.maxPathSum(
        root) == 3, "First case wrong zigzagLevelOrder result"

    root.left.left = TreeNode(5)
    root.right.left = TreeNode(3)
    assert solution.maxPathSum(
        root) == 10, "Second case wrong zigzagLevelOrder result"


if __name__ == "__main__":
    test()
