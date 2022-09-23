class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boats = 0
        left = 0
        right = len(people)-1
        while left<=right:
            if people[right] == limit:
                num_boats += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                num_boats += 1
                left += 1
                right -= 1
            else:
                num_boats += 1
                right -= 1
                if left == right:
                    num_boats += 1
                    break
        return num_boats
    