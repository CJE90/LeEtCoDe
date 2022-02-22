class MapNode:
    def __init__(self, value = 0):
        self.children = defaultdict(MapNode)
        self.value = value

class MapSum:

    def __init__(self):
        self.root = MapNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        curNode = self.root
        for c in key:
            curNode = curNode.children[c]
            curNode.value += diff
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        curNode = self.root
        for c in prefix:
            if c not in curNode.children:
                return 0
            curNode = curNode.children[c]
        return curNode.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

