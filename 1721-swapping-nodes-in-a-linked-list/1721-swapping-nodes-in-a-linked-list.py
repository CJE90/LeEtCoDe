# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        front = None
        
        while node:
            length+=1
            if length == k:
                front = node
            node = node.next
        back = head
        for i in range(length-k):
            back = back.next
            

        
       
            
        front.val, back.val = back.val, front.val
        return head
            
        
        