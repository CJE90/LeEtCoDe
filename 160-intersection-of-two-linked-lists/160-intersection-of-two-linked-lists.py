# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        diff = abs(lenA-lenB)
        
        if lenA > lenB:
            startLong = headA
            startShort = headB
        else:
            startLong = headB
            startShort = headA
            
        while diff > 0:
            startLong = startLong.next
            diff -= 1
        while startLong and startShort:
            if startLong == startShort:
                return startLong
            startLong = startLong.next
            startShort = startShort.next
        return None