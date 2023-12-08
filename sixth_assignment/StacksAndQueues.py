class stack:
    def __init__(self):
        self.items=[]
    def IsEmpty(self):
        # return self.items==[]
        if len(self.items)==0:
            return True
        else:
            return False
    def push(self,value):
        self.items.append(value)
    def pop(self):
        if self.items==0:
            return None
        else:
            return self.items.pop()
s=stack()
print("Please enter a word to check if it is a palindrom or not!")
x=input("")
print(x)
reversed_input=[]
list_input=[]
for i in x:
    s.push(i)
    list_input.append(i)
#creating the reversed of the input
while s.IsEmpty() != True:
    # s.pop()
    reversed_input = reversed_input + [s.pop()]
if reversed_input== list_input:
    print("Waw,",x, "is a palindrom!")
else:
    print(x, "is not a palindrom...")