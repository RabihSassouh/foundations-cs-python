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
        
s=stack()

def check(expression):
    #gather all open brackets
    for i in (expression):
        # for j in (expression):
        if i=='(' or i=='[' or i =='{':
            s.push(i)
    #check if each opened bracket have a closed bracket
        else:
            current=s.pop()
            if not s:
                return False
            if current=='(':
                if i!=')':
                    return False
            if current=='[':
                if i!=']':
                    return False
            if current=='{':
                if i!='}':
                    return False
    if s:
        return False
    return True        

print("please enter an expression to check if its brackets are balanced:")
expression=input("") 
check(expression)
print(s.items)
        
if s.items==[]:
    print("The expression you entered is balanced!")
else:
    print("The expression you entered is NOT balanced")