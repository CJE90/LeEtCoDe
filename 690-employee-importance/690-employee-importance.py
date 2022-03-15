"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lookup = {}
        for emp in employees:
            lookup[emp.id]=emp
        que = deque()
        que.append(lookup[id])
        returnValue = 0
        while que:
            emp = que.pop()
            returnValue += emp.importance
            for sub in emp.subordinates:
                que.append(lookup[sub])
        return returnValue