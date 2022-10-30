"""
Leetcode: https://leetcode.com/problems/delete-node-in-a-linked-list/
Date: 12-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            else:
                node = node.next


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    solution = Solution()
    solution.deleteNode(l1.next)
    assert l1.next.val == 3, "wrong deletion"
    assert l1.next.next == None, "wrong pointer"


if __name__ == "__main__":
    test()
