# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root.left, root.right])
        a = root.val
        b = float('inf')
        while queue:
            node = queue.pop()
            if not node:
                continue
            if node.val < a:
                a, b = node.val, a
            elif node.val < b and node.val != a:
                b = node.val
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
        return b if b != float('inf') else -1
        