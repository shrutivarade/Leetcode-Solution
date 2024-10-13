# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        newList = ListNode()
        ptr = newList

        if len(lists)==1:
            return lists[0]

        if lists:
            list1 = lists[0]

        for list2 in lists[1:]:
            while list1 and list2:
                if list1.val < list2.val:
                    ptr.next = list1
                    list1 = list1.next
                else:
                    ptr.next = list2
                    list2 = list2.next
                ptr = ptr.next

            if list1:
                while list1:
                    ptr.next = list1
                    list1 = list1.next
                    ptr = ptr.next
            else:
                while list2:
                    ptr.next = list2
                    list2 = list2.next
                    ptr = ptr.next

            list1 = newList.next
            ptr = newList
        

        return newList.next
        