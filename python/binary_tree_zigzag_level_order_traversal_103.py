"""
Leetcode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Date: 6-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        level = 1
        result = []
        queue = [root]
        while queue:
            queue_len = len(queue)
            level_result = []
            for i in range(queue_len):
                node = queue.pop(0)
                level_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                level_result.reverse()
            result.append(level_result)
            level += 1
        return result


def test():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2]], "First case wrong zigzagLevelOrder result"

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.right = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2], [4, 5, 7], [6]], "Second case wrong zigzagLevelOrder result"


if __name__ == "__main__":
    test()