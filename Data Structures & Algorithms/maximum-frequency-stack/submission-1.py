class FreqStack:

    def __init__(self):
        self.stacks=[]
        self.mp=defaultdict(lambda:-1)
        

    def push(self, val: int) -> None:
        idx=self.mp[val]+1
        while idx>=len(self.stacks):
            self.stacks.append([])
        self.stacks[idx].append(val)
        self.mp[val]+=1
        
    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if self.stacks:
            v= self.stacks[-1].pop()
            self.mp[v]-=1
            return v
        return -1
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()