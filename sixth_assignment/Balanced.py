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
print("please enter an expression to check if its brackets are balanced:")
expression=input("")
def check(expression):
    for i in (expression):
        for j in (expression):
            if i=='(' or i=='[' or i =='{':
                s.push(i)
                if j==')':
                    # for j in (s.items):
                    #     if j=='(':
                    return s.pop()
            # elif i==']':
            #     for j in (s.items):
            #         if j=='[':
            #             return s.pop()
            # elif i =='}':
            #     for j in (s.items):
            #         if j=='{':
            #             return s.pop()
                
check(expression)
print(s.items)
# if s.items==[]:
#     print("The expression you entered is balanced!")
# else:
#     print("The expression you entered is NOT balanced")