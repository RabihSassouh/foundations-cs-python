def mergeSort(list1,start,end):
    #base case
    if start==end:
        return
    mid=(start+end)//2
    mergeSort(list1,start,mid)
    mergeSort(list1,mid+1,end)
    merge(list1,start,mid,end)

def merge(list1,start,mid,end):
    new_list=[]
    ind1=start
    ind2=mid+1
    
    while ind1<=mid and ind2<=end:
        if list1[ind1]>list1[ind2]:
            new_list.append(list1[ind1])
            ind1+=1
        else:
            new_list.append(list1[ind2])
            ind2+=1
            
    while ind1<=mid:
        new_list.append(list1[ind1])
        ind1+=1
    while ind2<=end:
        new_list.append(list1[ind2])
        ind2+=1
    list1[start:end+1]=new_list

list1=[43,12,213,423,123,14]
mergeSort(list1,0,len(list1)-1)
print(list1)