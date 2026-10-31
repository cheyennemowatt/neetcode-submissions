# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        4 steps:
        1. save next_node (curr.next) to var so we don't lose access to it
        2. do the actual reversing step so curr.next points to prev
        3. move prev pointer
        4. move curr pointer
        5. return prev which would be end of list 
        """
        
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev