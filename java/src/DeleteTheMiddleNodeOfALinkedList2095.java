
/**
Leetcode: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Date: 12-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
*/
import java.util.Objects;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if (Objects.isNull(head) || Objects.isNull(head.next)) {
            return null;
        }
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;
        while (Objects.nonNull(fast) && Objects.nonNull(fast.next)) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = slow.next;
        slow.next = null;
        return head;
    }
}

public class DeleteTheMiddleNodeOfALinkedList2095 {

    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();

        ListNode ll = new ListNode(1);
        ll = solution.deleteMiddle(ll);
        if (Objects.nonNull(ll))
            throw new Exception("head deletion is non null");

        ll = new ListNode(1);
        ll.next = new ListNode(2);
        solution.deleteMiddle(ll);
        if (Objects.nonNull(ll.next))
            throw new Exception("head next deletion is non null");

        ll.next = new ListNode(2);
        ll.next.next = new ListNode(3);
        solution.deleteMiddle(ll);
        if (ll.val != 1 || ll.next.val != 3 || Objects.nonNull(ll.next.next))
            throw new Exception("head next deletion is non null");
    }
}