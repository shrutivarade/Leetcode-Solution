# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        returnHead = head

        if head.next == None:
            return None

        length = 0
        while head:
            length += 1
            head = head.next

        head = returnHead
        count = 0

        if(length == n):
            return head.next

        while head and count<(length-n):
            if count+1 == (length-n):
                head.next = head.next.next
                break

            count += 1
            head = head.next

            

        return returnHead