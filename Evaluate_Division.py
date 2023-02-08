class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        self.graph = defaultdict(list)
        for i in range(len(equations)):
            self.graph[equations[i][0]].append([equations[i][1], values[i]])
            self.graph[equations[i][1]].append([equations[i][0], 1/values[i]])
        result = []
        for query in queries:
            result.append(self.bfs(query[0], query[1]))
        return result
    def bfs(self, start, target):
            if start not in self.graph:
                return -1.0
            if start == target:
                return 1
            queue = deque([[start, 1]])
            visited = set()
            visited.add(start)
            while(queue):
                curr = queue.popleft()
                for child in self.graph[curr[0]]:
                    if child[0] not in visited:
                        if child[0] == target: return curr[1]*child[1]
                        queue.append([child[0], curr[1]*child[1]])
                        visited.add(child[0])
            return -1.0
