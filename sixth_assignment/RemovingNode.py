class Node:
  # constructor
  def __init__(self,value,next):
    self.value=value
    self.next=next


# a linked list is a list of nodes
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0 # the number of nodes in the LL
    
  def addAtHead(self,value): #O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else: # LL is not empty
      n.next=self.head
      self.head=n
      self.size+=1
      
  def addAtTail(self,value):#O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else:
      self.tail.next=n
      self.tail=n
      self.size+=1

  def deleteAtLocation(self,index): #O(n), n being the length of the list
    print("Please enter the location at which you want to delete the node:")
    index=int(input(""))
    if self.size==0:
      return None # LL is empty
    x=0
    temp=self.head # current keeps track of the node I am at
    while temp.next and x<index:
        prev=temp
        temp=temp.next
        x+=1
    if x==0:
        self.head=self.head.next
    elif x<index:
        print("The index you entered is out of range!")
    else:
        prev.next=temp.next

  def printLL(self):
    if self.size==0:
      print("my LL is empty")
    current=self.head
    while current!= None:
      print(current.value,"->",end=" ")
      current=current.next
    print()
ll=LinkedList()

ll.addAtHead(3)
ll.addAtHead(4)
ll.addAtHead(5)
ll.addAtHead(8)
ll.printLL()
try:
    ll.deleteAtLocation(2)
except:
    print("Please enter a valid integer!")
ll.printLL()

