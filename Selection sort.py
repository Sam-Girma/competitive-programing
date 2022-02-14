class Solution: 
    def select(self, arr, i):
        for tosort in range(i,len(arr)):
            for j in range (tosort+1,len(arr)):
                if arr[j] < arr[tosort]:
                    arr[tosort], arr[j] = arr[j], arr[tosort]
        
    
    def selectionSort(self, arr,n):
        for i in range(0, n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return(arr)
