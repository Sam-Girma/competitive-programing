class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        queue = deque([(0,0)])
        visited = set([(0,0)])
        level = 1
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0),(1, 1), (-1, -1), (-1, 1), (1, -1)]
        if grid[0][0] == 1:
            return -1
        if len(grid)==1:
            return 1
        def inbound(cell):
            return 0<=cell[0]<len(grid) and 0<=cell[1]<len(grid)
        while(queue):

            for i in range(len(queue)):
                curr = queue.popleft()
                for direc in directions:
                    neighbour_cell = (curr[0]+direc[0], curr[1]+direc[1])
                    if neighbour_cell in visited:
                        continue
                    if inbound(neighbour_cell) and grid[neighbour_cell[0]][neighbour_cell[1]]==0:
                        if neighbour_cell == (len(grid)-1, len(grid)-1):
                            return level+1
                        queue.append(neighbour_cell)
                        visited.add(neighbour_cell)
            level+=1
            print(queue)
        return -1             
