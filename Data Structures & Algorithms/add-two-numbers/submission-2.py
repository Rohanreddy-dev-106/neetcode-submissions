# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        s2 = ''

        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        #reverse the strings
        r_1=s1[::-1]
        r_2=s2[::-1]

        add_ans = int(r_1) + int(r_2)

        S_A = list(str(add_ans))
        S_A.reverse()

        dummy = ListNode(0)
        curr = dummy

        for i in S_A:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next