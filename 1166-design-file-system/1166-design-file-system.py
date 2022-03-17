class TrieNode: 
    def __init__(self, name):
        self.paths = {}
        self.contents = -1
        self.name = name
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        node = self.root
        components = path.split("/")
        for i in range(1, len(components)):
            name = components[i]
            
            if name not in node.paths:
                if i == len(components) - 1:
                    node.paths[name] = TrieNode(name)
                else:
                    return False
            node = node.paths[name]
        if node.contents != -1:
            return False
        node.contents = value
        return True

    def get(self, path: str) -> int:
        node = self.root
        components = path.split("/")
        for i in range(1, len(components)):
            name = components[i]
            if name not in node.paths:
                return -1
            node = node.paths[name]
        return node.contents
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)