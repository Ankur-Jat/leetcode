"""
Leetcode: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Date: 4-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = deque([root])
        sum_dict = {}
        while queue:
            node = queue.popleft()
            if node.val in sum_dict:
                return True
            sum_dict[k-node.val] = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


def test():
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)

    solution = Solution()
    assert solution.findTarget(root, 16) == True, "first test case failed"
    assert solution.findTarget(root, 36) == False, "first test case failed"


if __name__ == "__main__":
    test()
