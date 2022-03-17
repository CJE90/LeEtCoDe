class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.words.append(word)
            cur.words.sort()
            if len(cur.words) > 3:
                cur.words.pop()
    
    def search(self, currentString):
        cur = self.root
        result = []
        
        for c in currentString:
            if c not in cur.children:
                break
            cur = cur.children[c]
            result.append(cur.words[:])
        l_remain = len(currentString) - len(result)
        for _ in range(l_remain):
            result.append([])
        return result
    
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        return trie.search(searchWord)