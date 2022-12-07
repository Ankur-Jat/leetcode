"""
Leetcode: https://leetcode.com/problems/range-sum-of-bst/
Date: 7-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        self.recursiveSumBST(root, low, high)
        return self.sum

    def recursiveSumBST(self, node, low, high):
        if not node:
            return
        if low <= node.val <= high:
            self.sum += node.val
            self.recursiveSumBST(node.left, low, high)
            self.recursiveSumBST(node.right, low, high)
            return
        if node.val < low:
            return self.recursiveSumBST(node.right, low, high)
        else:
            self.recursiveSumBST(node.left, low, high)


def test():
    solution = Solution()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    assert solution.rangeSumBST(
        root, 7, 15) == 32, "First case wrong inorderTraversal result"

    root = TreeNode(1)
    assert solution.rangeSumBST(
        root, 7, 15) == 0, "Second case wrong inorderTraversal result"


if __name__ == "__main__":
    test()
