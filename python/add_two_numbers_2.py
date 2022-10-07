"""
Leetcode: https://leetcode.com/problems/add-two-numbers/
Date: 5-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sum_two_nodes(self, val1, val2, carry):
        sum_val = val1 + val2 + carry
        carry = sum_val // 10
        sum_val %= 10
        node = ListNode(sum_val)
        return node, carry
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        result_head = sum_ll = None
        carry = 0
        while ptr1 or ptr2:
            node, carry = self.sum_two_nodes(ptr1.val if ptr1 else 0, ptr2.val if ptr2 else 0, carry)
            if result_head:
                sum_ll.next = node
                sum_ll = node
            else:
                result_head = sum_ll = node
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        if carry:
            sum_ll.next, _ = self.sum_two_nodes(carry, 0, 0)
        return result_head
            
def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = Solution().addTwoNumbers(l1, l2)
    result = [7, 0, 8]
    for i in range(3):
        if not l3 or l3.val != result[i]:
            print("Test case failed at index: ", i)
            break
        l3 = l3.next

if __name__ == "__main__":
    test()