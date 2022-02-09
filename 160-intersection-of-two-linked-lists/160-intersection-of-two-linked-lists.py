# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = defaultdict(int)
        
        while headA:
            nodes[headA] += 1
            headA = headA.next
        
        while headB:
            if headB in nodes:
                return headB
            nodes[headB] += 1
            headB = headB.next

        return None