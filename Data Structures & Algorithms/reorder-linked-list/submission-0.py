# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        storage_list = []
        valid_list = []
        dummy_pointer = head

        while dummy_pointer:
            storage_list.append(dummy_pointer.val)
            dummy_pointer = dummy_pointer.next
        L = 0
        R = len(storage_list) - 1
        while L < R:
            valid_list.append(storage_list[L])
            valid_list.append(storage_list[R])
            L += 1
            R -= 1

        if L == R:
            valid_list.append(storage_list[L])

        dummy_pointer = head
        i = 0
        while dummy_pointer:
              dummy_pointer.val = valid_list[i]
              dummy_pointer = dummy_pointer.next
              i += 1