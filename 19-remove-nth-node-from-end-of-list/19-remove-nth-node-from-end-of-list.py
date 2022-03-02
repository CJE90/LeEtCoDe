# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        cur = head
        p = head
        while cur.next:
            count +=1
            cur = cur.next
            if count > n+1:
                p = p.next
        if count == n:
            return head.next
        else:
            p.next = p.next.next
            return head
        