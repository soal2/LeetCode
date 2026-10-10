"""
codetop.lc146 的 Docstring
https://leetcode.cn/problems/lru-cache/
"""
import sys
import json

class listNode:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUcache:
    def __init__(self, capacity):
        self.ht = {}
        self.capacity = capacity
        self.head = listNode()
        self.tail = listNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key:int, value:int) -> None:
        # node = listNode(key=key, val=value)
        if key in self.ht:
            self.move_node_to_tail(key=key)
            self.ht[key].val = value
        else:
            if len(self.ht) == self.capacity:
                # 删除头结点
                self.ht.pop(self.head.next.key)
                x = self.head.next
                self.head.next = x.next
                x.next.prev = self.head
            new_node = listNode(key=key, val=value)
            self.ht[key] = new_node
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            self.tail.prev = new_node

    def get(self, key:int) -> int:
        if key in self.ht:
            self.move_node_to_tail(key=key)
            return self.ht[key].val
        else:
            return -1

    def move_node_to_tail(self, key:int) -> None:
        node = self.ht[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

def main():
    data = sys.stdin.read().strip().splitlines()
    if len(data) < 2:
        return
    ops = json.loads(data[0].strip())
    params = json.loads(data[1].strip())
    res = []
    cache = None
    for op, args in zip(ops, params):
        if op == "LRUCache":
            cache = LRUcache(args[0])
            res.append(None)
        elif op == "put":
            cache.put(args[0], args[1])
            res.append(None)
        elif op == "get":
            res.append(cache.get(args[0]))
    print(json.dumps(res))

if __name__ == "__main__":
    main()