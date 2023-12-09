class Stack:
    def __init__(self,size=10):
        self.size=10
        self.s=[]
    def push(self,val):
        if len(self.s)<10:
            self.s.append(val)
    def pop(self):
        if len(self.s)!=0:
            return self.s.pop()
    def peek(self):
        if len(self.s) !=0:
            return self.s[-1]
    def isEmpty(self):
        return len(self.s)==0
    def getSize(self):
        return len(self.s)
    def __str__(self):
        return f"{self.s}"

s= Stack()
s.push(10)
s.push(43)
s.push(50)
s.push(100)
print(s)
s.pop()
print(s)
print(s.peek())
print(s.isEmpty())
print(s.getSize())

    