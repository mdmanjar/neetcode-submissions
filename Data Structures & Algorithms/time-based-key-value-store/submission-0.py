class TimeMap:

    def __init__(self):
        self.map={}

    def set(self,key,value,timestamp):
        if key not in self.map:
            self.map[key]=[]
        self.map[key].append((timestamp,value))

    def get(self,key,timestamp):
        if key not in self.map:
            return ""

        temp=self.map[key]
        start=0
        end=len(temp)-1

        while end-start>1:
            mid=start+(end-start)//2
            if temp[mid][0]>timestamp:
                end=mid
            else:
                start=mid

        if temp[end][0]<=timestamp:
            return temp[end][1]
        if temp[start][0]<=timestamp:
            return temp[start][1]
        return ""