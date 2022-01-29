class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dictt={}
        lst_of_frequency=[]
        arr.sort()
        for i in range(len(arr)):
            dictt[arr[i]]=0
        for i in range(len(arr)):
            dictt[arr[i]]+=1
        for i in dictt:
            lst_of_frequency.append(dictt[i])
        lst_of_frequency.sort()
        lst_of_frequency.reverse()
        counter=0
        summer=0
        iterator=0
        while(summer<(len(arr)/2)):
            summer+=lst_of_frequency[iterator]
            counter+=1
            iterator+=1
        return counter
           
