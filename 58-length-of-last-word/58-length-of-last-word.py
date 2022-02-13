class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        newArr = list(filter(lambda x: (x!= ''), arr))
        return len(newArr[len(newArr)-1])
        
        