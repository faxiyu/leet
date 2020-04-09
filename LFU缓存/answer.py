class Node:
    __slots__ = 'key', 'val', 'cnt'

    def __init__(self, key, val, cnt=0):
        self.key, self.val, self.cnt = key, val, cnt

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.cnt2node = defaultdict(OrderedDict)
        self.mincnt = 0


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        del self.cnt2node[node.cnt][key]

        if not self.cnt2node[node.cnt]:
            del self.cnt2node[node.cnt]
        node.cnt +=1
        self.cnt2node[node.cnt][key] = node

        if not self.cnt2node[self.mincnt]:
            self.mincnt +=1
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 :
            return
        if key in self.dic:
            self.dic[key].val = value
            self.get(key)
            return
        if len(self.dic) >= self.capacity:
            pop_key,_pop_node = self.cnt2node[self.mincnt].popitem(last=False)
            del self.dic[pop_key]
        
        self.dic[key] = self.cnt2node[1][key] = Node(key,value,1)
        self.mincnt = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)