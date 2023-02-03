# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = {}
        res = []
        if not root:
            return []
        queue = deque([[root, 0]])
        
        while(queue):
            cur_level = {}
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr[1] in cur_level:
                    cur_level[curr[1]].append(curr[0].val)
                else:
                    cur_level[curr[1]] = [curr[0].val]
                if curr[0].left:
                    queue.append([curr[0].left, curr[1]-1])
                if curr[0].right:
                    queue.append([curr[0].right, curr[1]+1])
            for i in cur_level:
                if i in levels:
                    levels[i]+=sorted(cur_level[i])
                else:
                    levels[i] = sorted(cur_level[i])
        
        for i in sorted(levels.keys()):
            
            res.append(levels[i])
        return res
            
        
            
            
        
        
