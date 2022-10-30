"""
Leetcode: https://leetcode.com/problems/path-sum/
Date: 6-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val > targetSum:
            return False
        if root.val == targetSum:
            if not root.left and not root.right:
                return True
            return False
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.hasPathSum(root, 3) == True, "First case wrong hasPathSum result"

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.right = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.hasPathSum(root, 15) == True, "Second case wrong hasPathSum result"
    assert solution.hasPathSum(root, 9) == False, "Second case wrong hasPathSum result"


if __name__ == "__main__":
    test()