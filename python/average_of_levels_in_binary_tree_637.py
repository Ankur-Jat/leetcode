"""
Leetcode: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Date: 2-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level_avg = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_sum = 0
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_avg.append(level_sum / (level_size * 1.0))
        return level_avg


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.averageOfLevels(root) == [1, 2.5], "First case wrong inorderTraversal result"

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(1)
    root.right.left.right = TreeNode(6)
    assert solution.averageOfLevels(root) == [1, 2.5, 3.3333333333333335, 6.0], "Second case wrong inorderTraversal result"


if __name__ == "__main__":
    test()
