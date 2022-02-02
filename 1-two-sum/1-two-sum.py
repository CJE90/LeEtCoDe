class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashTable = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hashTable:
                res.append(hashTable[nums[i]])
                res.append(i)
                return res
            compliment = target-nums[i]
            hashTable[compliment] = i
        return res
        