class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2):
            for ch in s1:
                if ch in s2:
                    return False
            return True
        maxProduct = 0
        for word1 in words:
            for word2 in words:
                if word1 != word2 and no_common_letters(word1, word2):
                    maxProduct = max(maxProduct, len(word1)*len(word2))
        return maxProduct
        