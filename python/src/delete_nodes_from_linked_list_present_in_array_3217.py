"""
Leetcode: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array
Date: 2-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from typing import List, Optional


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        ptr = head
        prev = None
        while ptr:
            if ptr.val in nums_set:
                if ptr == head:
                    head = head.next
                else:
                    prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return head

def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    solution = Solution()
    l2 = solution.modifiedList([4], l1)
    assert l2.val == 2, "wrong deletion"
    assert l2.next.val == 3, "wrong pointer"


if __name__ == "__main__":
    test()
