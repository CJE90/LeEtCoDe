class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.isWord = True
        
    def search(self, word):
        curNode = self.root
        possibleReplace = ""
        for c in word:
            if c not in curNode.children:
                if curNode.isWord:
                    return possibleReplace
                else:
                    return ""
            
            possibleReplace=possibleReplace+c
            
            curNode = curNode.children[c]
            if curNode.isWord:
                return possibleReplace
        return ""
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(' ')
        for index,word in enumerate(words):
            possibleWord = trie.search(word)
            if possibleWord != "":
                words[index] = possibleWord
            
        return " ".join(words)
        
        
        