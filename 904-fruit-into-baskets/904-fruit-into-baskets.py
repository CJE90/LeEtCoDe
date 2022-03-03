class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        pickedFruits = defaultdict(int)
        l = 0
        maxLength = 0
        for r in range(len(fruits)):
            pickedFruits[fruits[r]] += 1
            while len(pickedFruits) > 2:
                pickedFruits[fruits[l]] -= 1
                if pickedFruits[fruits[l]] < 1:
                    pickedFruits.pop(fruits[l])
                l += 1
            maxLength = max(maxLength, r-l+1)
        return maxLength
                
        