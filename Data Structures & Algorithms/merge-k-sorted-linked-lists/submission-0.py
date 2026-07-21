# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []

        for head in lists:
            while head:
                ans.append(head.val)
                head = head.next

        ans.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in ans:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
        