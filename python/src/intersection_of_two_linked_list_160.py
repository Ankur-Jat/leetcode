"""
Leetcode: https://leetcode.com/problems/intersection-of-two-linked-lists/
Date: 2-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_ll_len(ll):
            ll_len = 0
            ptr = ll
            while ptr:
                ll_len += 1
                ptr = ptr.next
            return ll_len
        
        headALen = get_ll_len(headA)
        headBLen = get_ll_len(headB)
        ptrA = headA
        ptrB = headB
        while headALen > headBLen and ptrA:
            ptrA = ptrA.next
            headALen -= 1
        while headALen < headBLen and ptrB:
            ptrB = ptrB.next
            headBLen -= 1
        while ptrA and ptrB and ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        if ptrA and ptrB and ptrA == ptrB:
            return ptrA
        return None


def test():
    l1 = ListNode(2)
    inter = ListNode(4)
    l1.next = inter
    l1.next.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = inter
    l2.next.next.next = ListNode(5)
    l3 = Solution().getIntersectionNode(l1, l2)
    assert l3 == l1.next, "Invalid intersection result"

    l2.next = ListNode(4)
    l3 = Solution().getIntersectionNode(l1, l2)
    assert l3 == None, "Invalid intersection result"

if __name__ == "__main__":
    test()