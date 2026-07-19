# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L= ListNode(0)
        h=L
        reverse_linkedlist=[]
        while head:
              reverse_linkedlist.append(head.val)
              head=head.next
        reverse_linkedlist.reverse()
        for i in  reverse_linkedlist:
            L.next=ListNode(i)
            L=L.next

        return h.next

        

        