def countingSort(arr):
    lst=100*[0]
    for i in range (len(arr)):
        lst[arr[i]]+=1
    return lst
            
