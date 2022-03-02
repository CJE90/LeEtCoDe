# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddhead = ListNode(0)
        evenhead = ListNode(0)
        evens = evenhead
        odds = oddhead
        isOdd = True
        node = head
        
        while node:
            if isOdd:
                odds.next = node
                odds = odds.next
            else:
                evens.next = node
                evens = evens.next
            isOdd = not isOdd
            node = node.next
        evens.next = None
        odds.next = evenhead.next
        return oddhead.next
        
                
            
        