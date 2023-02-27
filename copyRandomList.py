"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        heap = {None: None}
    
    
        curr = head
        while curr:
            copy = Node(curr.val)
            heap[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = heap[curr]
            copy.next = heap[curr.next]
            copy.random = heap[curr.random]

            curr = curr.next

        return heap[head]
