class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        answer = []
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                answer.append(l+1)
                answer.append(r+1)
                return answer
            elif curSum < target:
                l+=1
            else:
                r-=1
        return []
        