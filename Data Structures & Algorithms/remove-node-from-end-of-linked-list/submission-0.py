class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        size = 0
        temp_pointer = head
        while h is not None:
            size += 1
            h = h.next

        remove_nth = size - n

        # Remove the first node
        if remove_nth == 0:
            return head.next

        for i in range(remove_nth - 1):
            temp_pointer = temp_pointer.next

        temp_pointer.next = temp_pointer.next.next

        return head