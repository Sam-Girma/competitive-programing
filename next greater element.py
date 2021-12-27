class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        retlst=[]
        lst=[]
        dicti={}
        for i in range(len(nums2)):
            if len(lst)==0:
                lst.append(nums2[i])
            else:
                
                while(len(lst)!=0 and nums2[i]>lst[-1]):
                    dicti[lst.pop()]=nums2[i]
                lst.append(nums2[i])
        for i in range(len(lst)):
            dicti[lst[i]] = -1
        for i in range (len(nums1)):
            retlst.append(dicti[nums1[i]])
        return retlst
