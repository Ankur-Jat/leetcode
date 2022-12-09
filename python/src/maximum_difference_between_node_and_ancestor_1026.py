"""
Leetcode: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
Date: 9-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diff = float('-inf')
        self.recursiveMaxAncestorDiff(root)
        return self.max_diff

    def recursiveMaxAncestorDiff(self, node):
        if node.left:
            left_min, left_max = self.recursiveMaxAncestorDiff(node.left)
        else:
            left_min, left_max = node.val, node.val
        if node.right:
            right_min, right_max = self.recursiveMaxAncestorDiff(node.right)
        else:
            right_min, right_max = node.val, node.val
        # print(node.val, left_min, left_max, right_min, right_max)
        min_val, max_val = min(left_min, right_min, node.val), max(
            left_max, right_max, node.val)
        self.max_diff = max(
            self.max_diff,
            abs(node.val - min_val),
            abs(node.val - max_val)
        )
        return min_val, max_val


def test():
    solution = Solution()

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    assert solution.maxAncestorDiff(
        root) == 7, "First case wrong result"


if __name__ == "__main__":
    test()
