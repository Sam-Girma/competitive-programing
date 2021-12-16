def insertionSort1(n, arr):
    x=arr[-1]
    while (n>1):
        if x<arr[n-2]:
            arr[n-1]=arr[n-2]
            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()
        else:
            arr[n-1]=x
            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()
            break
        if (n==2):
            arr[0]=x
            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()
        n=n-1
