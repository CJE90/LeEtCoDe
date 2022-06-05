# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.find_middle(head)
        node = self.reverse_nodes(mid)
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
    
    def find_middle(self,node):
        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse_nodes(self,node):
        prev = None
        while node:
            cur = node
            node = node.next
            cur.next = prev
            prev = cur
        return prev
        
        