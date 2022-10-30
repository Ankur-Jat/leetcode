"""
Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Date: 12-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val == root.val or q.val == root.val:
            return root
        if (root.val > p.val) and (root.val > q.val) and root.left != None:
            return self.lowestCommonAncestor(root.left, p, q)
        if (root.val < p.val) and (root.val < q.val) and root.right != None:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


def test():
    solution = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert solution.lowestCommonAncestor(root, TreeNode(1), TreeNode(3)).val == 2, "First case wrong lowestCommonAncestor result"

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    assert solution.lowestCommonAncestor(root, TreeNode(7), TreeNode(6)).val == 7, "Second case wrong lowestCommonAncestor result"


if __name__ == "__main__":
    test()