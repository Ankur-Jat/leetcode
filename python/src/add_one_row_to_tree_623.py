"""
Leetcode: https://leetcode.com/problems/add-one-row-to-tree/
Date: 4-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder_traversal(self):
        return self.__recursive_inorder__()

    def __recursive_inorder__(self, result=None):
        if result == None:
            result = []
        if self.left:
            self.left.__recursive_inorder__(result)
        result.append(self.val)
        if self.right:
            self.right.__recursive_inorder__(result)
        return result


class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        self.recursiveAddOneRow(root, depth-1, val)
        return root

    def recursiveAddOneRow(self, node, depth, val):
        if not node:
            return
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = node.left
            node.left = new_node
            new_node = TreeNode(val)
            new_node.right = node.right
            node.right = new_node
        else:
            self.recursiveAddOneRow(node.left, depth-1, val)
            self.recursiveAddOneRow(node.right, depth-1, val)


def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    solution = Solution()
    solution.addOneRow(root, 5, 4)
    assert root.left.left.left.val == 5, "4th left should be 5"
    assert root.left.left.right.val == 5, "4th right should be 5"
    result = solution.addOneRow(root, 6, 1)
    assert result.val == 6, "root val must be 6"
    assert result.right == None, "root's right must be null"
    assert result.left == root, "root's left must be actual root"


if __name__ == "__main__":
    test()
