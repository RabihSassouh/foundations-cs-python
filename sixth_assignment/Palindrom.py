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
print("Please enter a word to check if it is a palindrom or not!")
x=input("")
list_input=[]
reversed_input=[]

for i in x: #O(n), where in is the len(x)
    s.push(i)
    list_input.append(i)

#creating the reversed of the input
while s.IsEmpty() != True:  
    reversed_input = reversed_input + [s.pop()]
if reversed_input== list_input:
    print("Waw,",x, "is a palindrom!")
else:
    print(x, "is not a palindrom...")