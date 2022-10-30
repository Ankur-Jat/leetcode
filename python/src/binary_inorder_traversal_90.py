"""
Leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/
Date: 6-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution(object):
    def recursive_inorder(self, node, result):
        if not node:
            return
        self.recursive_inorder(node.left, result)
        result.append(node.val)
        self.recursive_inorder(node.right, result)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recursive_inorder(root, result)
        return result


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.inorderTraversal(root) == [2, 1, 3], "First case wrong inorderTraversal result"

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.right = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.inorderTraversal(root) == [4, 2, 1, 5, 6, 3, 7], "Second case wrong inorderTraversal result"


if __name__ == "__main__":
    test()