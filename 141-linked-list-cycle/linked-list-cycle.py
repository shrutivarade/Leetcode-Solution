# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # HashSet, 
        # visited = set()
        # curr = head
        # while curr:
        #     if curr not in visited:
        #         visited.add(curr)
        #         curr = curr.next
        #     else:
        #         return True
        # return False

        # Floyd's Tortoise and Hare approach, slow and fast pointers
        
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if(s==f):
                return True


        return False