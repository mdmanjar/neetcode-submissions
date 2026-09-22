class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mp={}
        self.capacity=capacity
        self.size=0

    def add(self,node):
        node.next=self.head.next
        node.next.prev=node
        node.prev=self.head
        self.head.next=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key not in self.mp:return -1
        x=self.mp[key]
        self.remove(x)
        self.add(x)
        return x.val

    def put(self, key: int, value: int) -> None:

        if key not in self.mp:
            x=Node(key,value)
            self.mp[key]=x
            self.size+=1

        else:
            x=self.mp[key]
            x.val=value
            self.remove(x)

        self.add(x)

        if self.size>self.capacity:
            self.size-=1
            x=self.tail.prev
            del self.mp[x.key]
            self.remove(x)
