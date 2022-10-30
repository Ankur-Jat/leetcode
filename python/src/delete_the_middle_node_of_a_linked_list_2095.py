"""
Leetcode: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Date: 12-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        prev, slow, fast = None, head, head.next
        while fast:
            prev, slow, fast = slow, slow.next, fast.next
            if fast:
                fast = fast.next
        prev.next, slow.next = slow.next, None
        return head


def test():
    solution = Solution()
    l1 = ListNode(2)
    l2 = solution.deleteMiddle(l1)
    assert l2 == None, "invalid head deletion"
    l1 = ListNode(2)
    l1.next = ListNode(3)
    solution.deleteMiddle(l1)
    assert l1.next == None, "invalid head.next deletion"
    assert l1.val == 2, "invalid head.next deletion"
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)
    l1.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next = ListNode(7)
    l2 = solution.deleteMiddle(l1)
    assert l1.next.next.val == 4, "invalid mid deletion"
    assert l1.next.next.next.val == 6, "invalid mid next value"


if __name__ == "__main__":
    test()
