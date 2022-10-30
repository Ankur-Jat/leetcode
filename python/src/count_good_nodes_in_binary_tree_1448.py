"""
Leetcode: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Date: 1-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root, max_so_far = float('-inf')):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum_val = 1 if root.val >= max_so_far else 0
        max_so_far = max(root.val, max_so_far)
        return sum_val + self.goodNodes(root.left, max_so_far) + self.goodNodes(root.right, max_so_far)


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.goodNodes(root) == 3, "First case wrong inorderTraversal result"

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.right = TreeNode(6)
    root.right.right = TreeNode(1)
    assert solution.goodNodes(root) == 6, "Second case wrong inorderTraversal result"


if __name__ == "__main__":
    test()
