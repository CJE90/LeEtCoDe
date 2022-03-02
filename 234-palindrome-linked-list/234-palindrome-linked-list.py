# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next
        left = 0
        right = len(l)-1
        while left<right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True
        