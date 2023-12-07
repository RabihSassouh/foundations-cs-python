class stack:
    def __init__(self):
        self.items=[]
    def IsEmpty(self):
        if self.items==0:
            return None
    def push(self,value):
        self.items.append(value)
    def pop(self):
        if self.items==0:
            return None
        else:
            return self.items.pop()
        