class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prevTemp = stack.pop()
                result[prevTemp] = i-prevTemp 
            stack.append(i)
        return result