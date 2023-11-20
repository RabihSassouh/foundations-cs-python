# function: insertion sort
# params: list1: a list of items to sort
# it sorts the elements of list1
def insertionSort(list1): #O(n^2)
  border=1
  while border<len(list1): #O(n), n being the length of the list
    current=border # the index of the element we are currently dealing with
    while current>0 and list1[current]<list1[current-1]: #O(n)
      # swap the out of order elements
      # temp=list1[current]
      # list1[current]=list1[current-1]
      # list1[current-1]=temp
      list1[current],list1[current-1]=list1[current-1],list1[current] #O(1)
      current-=1
    border+=1

  print(list1)

list1=['c','a','Z','m']
insertionSort(list1)