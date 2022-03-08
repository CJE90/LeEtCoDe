class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        def backtrack(index,path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            possibleLetters = letters[digits[index]]
            for letter in possibleLetters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
            
        
        result = []
        backtrack(0, [])
        return result