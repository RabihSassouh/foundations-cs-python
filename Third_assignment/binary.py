try:
    n=int(input('Please enter the length of the binary list you want to get: '))
    def binary_list(n):
        result=[]
        x=''
        def temp_list(x,n,result):
            if n>0:
                temp_list((x+"0"),n-1,result)
                temp_list((x+"1"),n-1,result)
            else:
                result.append(x)
                return result
        temp_list(x,n,result)
        return result
    print(binary_list(n))
except:
    print("The character you entered is not valid, please enter a postiver integer and try again.")