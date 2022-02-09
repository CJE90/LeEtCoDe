# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        node = head
        newNext = None
        while node:
            stack.append(node)
            node = node.next
        
        stackSize = len(stack)
        if n == stackSize:
            return head.next
        i = 0
        while i< stackSize:
            i +=1
            tmp = stack.pop()
            if i == n-1:
                newNext = tmp
            if i == n+1:
                tmp.next = newNext
                return head
        
                
        
        
        