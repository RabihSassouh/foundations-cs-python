#class stack
class stack:
    def __init__(self):
        self.items=[]

#funtion IsEmpty returns true if the stack is empty
    def IsEmpty(self):  #O(1)
        if len(self.items)==0:
            return True
        else:
            return False

#function push addes items to the stack
#params: value (value is the item to be added)
    def push(self,value):   #O(1)
        self.items.append(value)

#function pop returns the value deleted from the class
    def pop(self):  #O(1)
        if self.items==0:
            return None
        else:
            return self.items.pop()

#taking the input from the user and adding it to the stack
s=stack()
print("message to encode:")
x=input("")

#filling the stack and reversing when reaching asterix
def decode(x):
    reverse_input=''
    for i in x: #O(n), where in is the len(x)
        if i.isalpha() or i.isspace():
            s.push(i)
        elif i=='*':
             while s.IsEmpty() != True:
                reverse_input =reverse_input + s.pop()
        else:
            return
    print(reverse_input)
decode(x)


