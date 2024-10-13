# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return
        # find middle
        slow = fast = head

        # node can point to null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part of linkedlist [1,2] [4,3]
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merge the two list [1,4,2,3]

        l1, l2 = head, prev
        while l2.next:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l1 = tmp1
            l2.next = l1
            l2 = tmp2
        return head

