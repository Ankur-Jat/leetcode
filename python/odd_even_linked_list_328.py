"""
Leetcode: https://leetcode.com/problems/odd-even-linked-list/
Date: 5-Aug-2022
Author: Ankur Jat
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even_backup, even = head.next, head.next
        while even and even.next:
            odd.next = even.next
            even.next = odd.next.next
            if odd.next:
                odd = odd.next
            even = even.next
        odd.next = even_backup
        return head

def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = Solution().oddEvenList(l1)
    result = [2, 3, 4]
    for i in range(3):
        if not l2 or l2.val != result[i]:
            print("First Test case failed at index: ", i)
            break
        l2 = l2.next

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(5)
    l2 = Solution().oddEvenList(l1)
    result = [2, 3, 4, 5]
    for i in range(4):
        if not l2 or l2.val != result[i]:
            print("Second Test case failed at index: ", i)
            break
        l2 = l2.next

if __name__ == "__main__":
    test()