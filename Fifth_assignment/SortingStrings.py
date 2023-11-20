def selectionSort(list1): #O(n^2)
  border=0
  while border <len(list1)-1: #O(n), n being the length of the list
    minIndex=border # contain the index of the minimum element
    for i in range(border+1, len(list1)): # to find the index of the minimum element, O(n)
      list1[i]=list1[i].lower()
      if list1[i]<list1[minIndex]: #O(1), is the line that specifies the order
        minIndex=i
    #swap the two elements
    temp=list1[border] #O(1)
    list1[border]=list1[minIndex]
    list1[minIndex]=temp

    # list1[border],list1[minIndex]=list1[minIndex],list1[border]

    border=border+1

  print(list1)
list1=['e','A','b','Z','a']
selectionSort(list1)
