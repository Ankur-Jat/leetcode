"""
Leetcode: https://leetcode.com/problems/leaf-similar-trees
Date: 8-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node, leaf_nodes):
            if not node:
                return
            if not node.left and not node.right:
                return leaf_nodes.append(node.val)
            dfs(node.left, leaf_nodes)
            dfs(node.right, leaf_nodes)
        root1_leaves, root2_leaves = [], []
        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)
        return root1_leaves == root2_leaves


def test():
    solution = Solution()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(9)
    root2.right.left = TreeNode(7)
    root2.right.right = TreeNode(18)
    assert solution.leafSimilar(
        root, root2) == True, "First case wrong result"
    root2.right.right = None
    assert solution.leafSimilar(
        root, root2) == False, "Second case wrong result"


if __name__ == "__main__":
    test()
