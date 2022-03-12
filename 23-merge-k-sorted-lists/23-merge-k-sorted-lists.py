# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        ListNode.__lt__ = lambda self, other: self.val < other.val
        dummyNode = ListNode(0)
        tail = dummyNode
        min_heap = []
        for n in lists:
            if n:
                heapq.heappush(min_heap, (n.val, n))
        while min_heap:
            val,curNode = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next
            if curNode.next != None:
                heapq.heappush(min_heap, (curNode.next.val, curNode.next))
        return dummyNode.next











































#         ListNode.__lt__ = lambda self, other: self.val < other.val
#         min_heap = []
#         head = tail = ListNode(0)
        
#         for i in lists:
#             if i:
#                 heapq.heappush(min_heap,(i.val, i))
#         while min_heap:
#             node = heapq.heappop(min_heap)[1]
#             tail.next = node
#             tail = tail.next
#             if node.next:
#                 heapq.heappush(min_heap,(node.next.val, node.next))
#         return head.next
        