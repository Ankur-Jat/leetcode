"""
Leetcode: https://leetcode.com/problems/middle-of-the-linked-list/
Date: 5-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_nodes_as_list(self):
        node = self
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(5)
    l1.next.next.next.next = ListNode(8)
    l2 = Solution().middleNode(l1)
    assert l2.get_nodes_as_list() == [3, 5, 8], "Failed the first assertion"
    l1.next.next.next.next.next = ListNode(9)
    l2 = Solution().middleNode(l1)
    assert l2.get_nodes_as_list() == [5, 8, 9], "Failed the second assertion"


if __name__ == "__main__":
    test()
