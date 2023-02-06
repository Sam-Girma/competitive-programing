class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) #position, velocity, num_steps
        
        visited = set()
            
        while queue:
            cur_pos, cur_speed, cur_steps = queue.popleft()
            if cur_pos == target:
                return cur_steps
            if (cur_pos, cur_speed) in visited:
                continue
            visited.add((cur_pos, cur_speed))
            queue.append((cur_pos + cur_speed, cur_speed * 2, cur_steps + 1))
            if cur_speed > 0:
                queue.append((cur_pos, -1, cur_steps + 1))
            else:
                queue.append((cur_pos, 1, cur_steps + 1))
