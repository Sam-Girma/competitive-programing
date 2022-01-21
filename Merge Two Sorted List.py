# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        def myFunc(e):
            return e.val
        while(list1!=None):
            lst.append(list1)
            list1=list1.next
        while(list2!=None):
            lst.append(list2)
            list2=list2.next
        if len(lst)==0:
            return None
        lst.sort(key=myFunc)
        for i in range(len(lst)):
            if i!=len(lst)-1:
                lst[i].next=lst[i+1]
            else:
                lst[i].next=None
        
        head=lst[0]
        return head
