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
        def explore(employee):
            if len(employee.subordinates) == 0:
                return employee.importance
            curImportance = 0
            for sub in employee.subordinates:
                curImportance += explore(lookup[sub])
            return employee.importance + curImportance
        
        
        return explore(lookup[id])