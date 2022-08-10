"""
Leetcode: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Date: 10-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def inorder(self, result=None):
        if result == None:
            result = []
        if self.left:
            self.inorder(self.left)
        result.append(self.val)
        if self.right:
            self.inorder(self.right)
        return result

    def bfs(self):
        result = []
        queue = deque([self])
        while queue:
            node = queue.popleft()
            if not node:
                result.append(None)
            else:
                result.append(node.val)
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return result


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createTree(nums)
    
    def createTree(self, nums):
        if not nums:
            return None
        index = len(nums) / 2
        node = TreeNode(nums[index])
        node.left = self.createTree(nums[0:index])
        node.right = self.createTree(nums[index+1:])
        return node


def test():
    solution = Solution()

    testcases = [
        [ [-10,-3,0,5,9], [0,-3,9,-10,None,5, None] ],
        [ [1, 3], [3, 1, None] ]
    ]
    for index, testcase in enumerate(testcases):
        result = solution.sortedArrayToBST(testcase[0]).bfs()
        assert solution.sortedArrayToBST(testcase[0]).bfs() == testcase[1], "Testcase: {} failed".format(index)


if __name__ == "__main__":
    test()