# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headc=head
        c=0
        lst=[]
        while(headc!=None):
            c+=1
            lst.append(headc)
            headc=headc.next
        if c<=1:
            return head
        no_of_swaps=c//2
        i=0
        swaps=0
        while(swaps<no_of_swaps):
            lst[i],lst[i+1]=lst[i+1],lst[i]
            i+=2
            swaps+=1
        for i in range(len(lst)):
            if i!=len(lst)-1:
                lst[i].next=lst[i+1]
            else:
                lst[i].next=None
        head=lst[0]
        return head
 
