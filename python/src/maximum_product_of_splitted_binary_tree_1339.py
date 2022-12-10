"""
Leetcode: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
Date: 10-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            node.totalSum = leftSum + rightSum + node.val
            return node.totalSum

        def getMaxProductSum(node):
            if node.left:
                self.maxProduct = max(
                    self.maxProduct,
                    node.left.totalSum * (self.treeSum - node.left.totalSum)
                )
                getMaxProductSum(node.left)
            if node.right:
                self.maxProduct = max(
                    self.maxProduct,
                    node.right.totalSum * (self.treeSum - node.right.totalSum)
                )
                getMaxProductSum(node.right)

        self.treeSum = dfs(root)
        self.maxProduct = float('-inf')
        getMaxProductSum(root)
        return self.maxProduct % (10**9 + 7)


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
    assert solution.maxProduct(
        root) == 696, "First case wrong result"


if __name__ == "__main__":
    test()
