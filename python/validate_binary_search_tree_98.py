
"""
Leetcode: https://leetcode.com/problems/validate-binary-search-tree/
Date: 11-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root, min=float('-inf'), max=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return min < root.val < max and self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)


def test():
    solution = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert solution.isValidBST(root) == True, "First case wrong zigzagLevelOrder result"

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert solution.isValidBST(root) == False, "Second case wrong zigzagLevelOrder result"


if __name__ == "__main__":
    test()
