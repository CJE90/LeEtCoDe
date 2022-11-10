class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        max_answer = 0
        left = 0
        tokens.sort()
        right = len(tokens)-1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                ans += 1
                left += 1
                max_answer = max(max_answer, ans)
            elif ans > 0:                
                    power += tokens[right]
                    ans -= 1
                    right -= 1
                    max_answer = max(max_answer, ans)
            else:
                return 0
        return max_answer
                
        